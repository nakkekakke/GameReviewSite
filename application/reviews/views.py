from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db
from application.reviews.models import Review
from application.reviews.forms import ReviewForm
from application.games.models import Game

@app.route('/reviews/new/<game_id>/', methods=['GET'])
@login_required
def reviews_form(game_id):
    game = Game.query.get(game_id)
    if not game:
        return redirect(url_for('games_index'))

    return render_template('reviews/new.html',
        game = game,
        form = ReviewForm()
    )

@app.route('/reviews/<game_id>/', methods=['POST'])
@login_required
def reviews_create(game_id):
    game = Game.query.get(game_id)
    if not game:
        return redirect(url_for('games_index'))

    form = ReviewForm(request.form)
    if not form.validate():
        return render_template('reviews/new.html',
            game = game,
            form = form
    )

    review = Review(
        form.content.data,
        form.rating.data
    )
    review.game_id = game_id
    review.account_id = current_user.id

    db.session().add(review)
    db.session().commit()

    return redirect(url_for('games_index'))

@app.route('/reviews/<game_id>/', methods=['GET'])
@login_required
def reviews_show(game_id):
    game = Game.query.get(game_id)
    if not game:
        return redirect(url_for('games_index'))

    reviews = Game.find_reviews_of_game(game_id)

    return render_template('reviews/list.html',
        game = game,
        reviews = reviews
    )
    
    

    
