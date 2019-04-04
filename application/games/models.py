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
        stmt = text("SELECT review.content, review.rating"
                    " FROM review"
                    " WHERE review.game_id = :game_id"
        ).params(game_id = game_id)
        res = db.engine.execute(stmt)

        reviews = []
        for row in res:
            reviews.append({ "content": row[0], "rating": row[1] })

        return reviews

    def find_average_score(game_id):
        stmt = text("SELECT AVG(rating) FROM review"
                    " WHERE review.game_id = :game_id"
        ).params(game_id = game_id)

        res = db.engine.execute(stmt)
        print(vars(res))
        for row in res:
            return round(row[0], 2)

