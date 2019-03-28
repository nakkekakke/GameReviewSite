from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from datetime import datetime

class GameForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=30)])
    developer = StringField('Developer', [validators.Length(min=1, max=30)])
    year = IntegerField('Year', [validators.NumberRange(min=1950, max=datetime.now().year+1)])
    genre = StringField('Genre', [validators.Length(min=1, max=20)])

    class Meta:
        csrf = False
        