from flask import render_template, request, redirect, url_for
from application import app, db
from application.games.models import Game
from application.games.forms import GameForm

@app.route('/games/', methods=['GET'])
def games_index():
    return render_template('games/list.html', games = Game.query.all())

@app.route('/games/new/')
@login_required
def games_form():
    return render_template('/games/new.html', form = GameForm())

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
def game_view(id):
    return render_template('/games/show.html', game = Game.query.get(id))

@app.route('/games/<id>/', methods=['POST'])
@login_required
def game_update(id):
    newGame = constructGame(request.form)
    oldGame = Game.query.get(id)
    compareGamesAndUpdate(oldGame, newGame)
    db.session().commit()
    return redirect(url_for('game_view', id = oldGame.id))



# Helper methods

def constructGame(formData):
    return Game(
        formData.get('name'), 
        formData.get('developer'), 
        formData.get('year'), 
        formData.get('genre')
    )

def compareGamesAndUpdate(old, new):
    if old.name != new.name:
        old.name = new.name
    if old.developer != new.developer:
        old.developer = new.developer
    if old.year != new.year:
        old.year = new.year
    if old.genre != new.genre:
        old.genre = new.genre