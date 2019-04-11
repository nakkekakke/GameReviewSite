# Flask app
from flask import Flask
app = Flask(__name__)

# Database
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get('HEROKU'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviewapp.db'
    app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Login
from os import urandom
app.config['SECRET_KEY'] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'auth_login'
login_manager.login_message = 'Please login to use this functionality'

# login_required with roles
from functools import wraps

def login_required(role="NORMAL"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            if ((current_user.role != role) and (role != "NORMAL")):
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper



# Application functionality
from application import views
from application.games import models
from application.games import views
from application.reviews import models
from application.reviews import views
from application.auth import models
from application.auth import views

# Login part 2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Create db tables if they don't exist
try:
    db.create_all()
except:
    pass