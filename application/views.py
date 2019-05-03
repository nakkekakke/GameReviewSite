from flask import render_template
from application import app
from application.games.models import Game

@app.route('/')
def index():
    game = Game.find_highest_rated()
    return render_template('index.html', game = game)