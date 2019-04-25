from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators
from datetime import datetime

class GameForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=30)])
    developer = StringField('Developer', [validators.Length(min=1, max=30)])
    year = IntegerField('Year', [validators.NumberRange(min=1950, max=datetime.now().year+1)])
    category = SelectField('Category', choices=[(1, 'empty')], coerce=int)

    class Meta:
        csrf = False

class GameEditForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=30)])
    developer = StringField('Developer', [validators.Length(min=1, max=30)])
    year = IntegerField('Year', [validators.NumberRange(min=1950, max=datetime.now().year+1)])

    class Meta:
        csrf = False

class GameCategoryAddForm(FlaskForm):
    category = SelectField('Category', choices=[(1, 'empty')], coerce=int)

    class Meta:
        csrf = False
