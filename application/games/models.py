from application import db
from application.models import Base

from sqlalchemy.sql import text

class Game(Base):
    __tablename__ = 'game'

    name = db.Column(db.String(144), nullable=False)
    developer = db.Column(db.String(144), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(144))

    reviews = db.relationship('Review', backref='game', lazy=True)

    def __init__(self, name, developer, year, genre):
        self.name = name
        self.developer = developer
        self.year = year
        self.genre = genre

    @staticmethod
    def find_reviews_of_game(game_id):
        if not isinstance(game_id, int):
            return null

        stmt = text("SELECT review.content, review.rating"
                    " FROM review, game"
                    " WHERE game.id = review.id"
        )
        res = db.engine.execute(stmt)

        reviews = []
        for row in res:
            reviews.append({ "content": row[0], "rating": row[1] })

        return reviews
