from sqlalchemy.sql import text
from application import db
from application.models import Base
from application.games.models import Game

class User(Base):
    __tablename__ = 'account'

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)

    reviews = db.relationship('Review', backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.role = "NORMAL"
    
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def find_reviews(self):
        return self.reviews
