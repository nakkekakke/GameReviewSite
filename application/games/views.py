from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db
from application.games.models import Game
from application.games.forms import GameForm

@app.route('/games/', methods=['GET'])
def games_index():
    return render_template('games/list.html', games = Game.query.all())

@app.route('/games/new/')
@login_required
def games_form():
    return render_template('games/new.html', form = GameForm())

@app.route('/games/', methods=['POST'])
@login_required
def games_create():
    form = GameForm(request.form)

    if not form.validate():
        return render_template('games/new.html', form = form)

    game = Game(
        form.name.data,
        form.developer.data,
        form.year.data,
        form.genre.data
    )

    db.session().add(game)
    db.session().commit()
    return redirect(url_for('games_index'))

@app.route('/games/<id>/', methods=['GET'])
def games_view(id):
    game = Game.query.get(id)
    if not game:
        return redirect(url_for('games_index'))
    avg = Game.find_average_score(id)
    return render_template('games/show.html', game = game, avg = avg, form=GameForm())

@app.route('/games/<id>/', methods=['POST'])
@login_required
def games_update(id):
    newGame = GameForm(request.form)
    oldGame = Game.query.get(id)
    if (not newGame) or (not oldGame):
        return redirect(url_for('games_view', id = id))
    if not newGame.validate():
        avg = Game.find_average_score(id)
        return render_template('games/show.html', game = oldGame, avg = avg, form = newGame)
    compareGamesAndUpdate(oldGame, newGame)
    db.session().commit()
    return redirect(url_for('games_view', id = oldGame.id))

@app.route('/games/delete/<id>/', methods=['POST'])
@login_required
def games_delete(id):
    game = Game.query.get(id)
    if not game:
        return redirect(url_for('games_view', id = id))
    db.session().delete(game)
    db.session().commit()
    return redirect(url_for('games_index'))

# Helper methods

def constructGame(formData):
    return Game(
        formData.get('name'), 
        formData.get('developer'), 
        formData.get('year'), 
        formData.get('genre')
    )

def compareGamesAndUpdate(old, new):
    if old.name != new.name.data:
        old.name = new.name.data
    if old.developer != new.developer.data:
        old.developer = new.developer.data
    if old.year != new.year.data:
        old.year = new.year.data
    if old.genre != new.genre.data:
        old.genre = new.genre.data