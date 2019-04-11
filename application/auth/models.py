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

    @staticmethod
    def find_reviews_of_user(user_id): 
        stmt = text("SELECT review.content, review.rating, review.game_id"
                    " FROM review"
                    " WHERE review.account_id = :account_id"
        ).params(account_id = user_id)
        res = db.engine.execute(stmt)

        reviews = []
        for row in res:
            game = Game.query.get(row[2])
            reviews.append({ "content": row[0], "rating": row[1], "game": game})

        return reviews
