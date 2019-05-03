from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.games.models import Game
from application.games.forms import GameForm, GameEditForm, GameCategoryAddForm
from application.categories.models import Category

@app.route('/games/', methods=['GET'])
def games_index():
    return render_template('games/list.html', games = Game.query.all())


@app.route('/games/new/')
@login_required()
def games_form():
    form = GameForm()
    form.category.choices = getCategories()

    return render_template('games/new.html', form = form)


@app.route('/games/', methods=['POST'])
@login_required()
def games_create():
    form = GameForm(request.form)
    form.category.choices = getCategories()

    if not form.validate():
        return render_template('games/new.html', form = form)

    category = Category.query.get(form.category.data)

    game = Game(
        form.name.data,
        form.developer.data,
        form.year.data
    )

    game.categories.append(category)
    category.games.append(game)

    db.session().add(game)
    db.session().add(category)
    db.session().commit()
    return redirect(url_for('games_index'))


@app.route('/games/<id>/', methods=['GET'])
def games_view(id):
    game = Game.query.get(id)
    if not game:
        return redirect(url_for('games_index'))

    avg = Game.find_average_score(id)
    catform = newCatForm(id)

    return render_template('games/show.html',
        game = game,
        avg = avg,
        form = GameEditForm(),
        catform = catform
    )


@app.route('/games/<id>/', methods=['POST'])
@login_required(role="ADMIN")
def games_update(id):
    newGame = GameEditForm(request.form)
    oldGame = Game.query.get(id)

    if (not newGame) or (not oldGame):
        return redirect(url_for('games_index'))

    if not newGame.validate():
        avg = Game.find_average_score(id)
        return render_template('games/show.html',
            game = oldGame,
            avg = avg,
            form = newGame,
            catform = newCatForm()
        )

    compareGamesAndUpdate(oldGame, newGame)
    db.session().commit()

    return redirect(url_for('games_view', id = oldGame.id))


@app.route('/games/delete/<id>/', methods=['POST'])
@login_required(role="ADMIN")
def games_delete(id):
    game = Game.query.get(id)
    if not game:
        return redirect(url_for('games_index'))

    for review in game.reviews:
        db.session().delete(review)

    db.session().delete(game)
    db.session().commit()

    return redirect(url_for('games_index'))


@app.route('/games/<game_id>/catdelete/<category_id>/', methods=['POST'])
@login_required()
def games_category_delete(game_id, category_id):
    game = Game.query.get(game_id)
    category = Category.query.get(category_id)

    if category in game.categories:
        game.categories.remove(category)
        db.session().commit()

    return redirect(url_for('games_view', id = game_id))


@app.route('/games/<id>/catcreate/', methods=['POST'])
@login_required()
def games_category_create(id):
    form = GameCategoryAddForm(request.form)
    game = Game.query.get(id)
    category = Category.query.get(form.category.data)

    if not category in game.categories:
        game.categories.append(category)
        db.session().commit()

    return redirect(url_for('games_view', id = id))


# Helper methods

# Not in user right now
def constructGame(formData):
    return Game(
        formData.get('name'), 
        formData.get('developer'), 
        formData.get('year')
    )

def compareGamesAndUpdate(old, new):
    if old.name != new.name.data:
        old.name = new.name.data
    if old.developer != new.developer.data:
        old.developer = new.developer.data
    if old.year != new.year.data:
        old.year = new.year.data

def getCategories():
    categories = []
    for category in Category.query.all():
        categories.append((category.id, category.name))
    return categories

def newCatForm(game_id):
    catform = GameCategoryAddForm()
    game = Game.query.get(game_id)
    categories = []
    for category in Category.query.all():
        if not category in game.categories:
            categories.append((category.id, category.name))
    catform.category.choices = categories
    return catform