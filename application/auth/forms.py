from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField('Enter your name', [validators.Length(min=3, max=30)])
    username = StringField('Choose a username', [validators.Length(min=3, max=20)])
    password = PasswordField('Choose a password', [validators.Length(min=5, max=30)])

    class Meta:
        csrf = False
