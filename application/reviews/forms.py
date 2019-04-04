from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, validators

class ReviewForm(FlaskForm):
    content = TextAreaField('Content', [validators.Length(min=1, max=100)])
    rating = IntegerField('Rating', [validators.NumberRange(min=1, max=10)])

    class Meta:
        csrf = False