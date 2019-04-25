from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.reviews.models import Review
from application.reviews.forms import ReviewForm
from application.games.models import Game

@app.route('/reviews/new/<game_id>/', methods=['GET'])
@login_required()
def reviews_form(game_id):
    game = Game.query.get(game_id)
    if not game:
        return redirect(url_for('games_index'))

    return render_template('reviews/new.html',
        game = game,
        form = ReviewForm()
    )


@app.route('/reviews/game/<game_id>/', methods=['POST'])
@login_required()
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

    return redirect(url_for('reviews_show', game_id = game_id))


@app.route('/reviews/game/<game_id>/', methods=['GET'])
def reviews_show(game_id):
    game = Game.query.get(game_id)
    if not game:
        return redirect(url_for('games_index'))

    return render_template('reviews/list.html',
        game = game,
        reviews = game.find_reviews()
    )


@app.route('/reviews/<review_id>/edit/', methods=['GET'])
def reviews_editform(review_id):
    form = ReviewForm()
    review = Review.query.get(review_id)
    game = Game.query.get(review.game_id)

    if not (review and game):
        return redirect(url_for('games_index'))

    return render_template('reviews/edit.html',
        review = review,
        form = form,
        game = game
    )


@app.route('/reviews/<id>/edit/', methods=['POST'])
def reviews_edit(id):
    newReviewData = ReviewForm(request.form)
    oldReview = Review.query.get(id)

    if (not newReviewData) or (not oldReview):
        return redirect(url_for('games_index'))

    if not newReviewData.validate():
        return render_template('reviews/edit.html',
            review = oldReview,
            form = newReviewData
        )

    compareReviewsAndUpdate(oldReview, newReviewData)
    db.session().commit()
    return redirect(url_for('reviews_show', game_id = oldReview.game_id))


@app.route('/reviews/<id>/', methods=['POST'])
def reviews_delete(id):
    review = Review.query.get(id)
    game_id = review.game_id
    if review:
        db.session.delete(review)
        db.session().commit()

    return redirect(url_for('reviews_show', game_id = game_id))


# Helper methods

def compareReviewsAndUpdate(old, new):
    if old.content != new.content.data:
        old.content = new.content.data
    if old.rating != new.rating.data:
        old.rating = new.rating.data
    return old

    
    

    
