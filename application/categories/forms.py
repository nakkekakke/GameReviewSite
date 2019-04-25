from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CategoryForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=30)])

    class Meta:
        csrf = False
