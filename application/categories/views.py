from flask import render_template, request, redirect, url_for
from flask_login import current_user

from application import app, db, login_required
from application.categories.models import Category
from application.categories.forms import CategoryForm
from application.games.models import Game

@app.route('/categories/new/')
@login_required()
def categories_form():
    return render_template('categories/new.html', form = CategoryForm())

@app.route('/categories/', methods=['POST'])
@login_required()
def categories_create():
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template('categories/new.html', form = form)

    print(form.name.data)
    category = Category(form.name.data)

    form.name.errors.append(form.name.data + ' added!')

    db.session().add(category)
    db.session().commit()
    return render_template('categories/new.html', form = form)