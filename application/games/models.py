from sqlalchemy.sql import text
from application import db
from application.models import Base


game_category = db.Table('gamecategory', Base.metadata,
    db.Column('game_id', db.Integer,
        db.ForeignKey('game.id'),
        nullable=False
    ),
    db.Column('category_id', db.Integer,
        db.ForeignKey('category.id'),
        nullable=False
    )
)

class Game(Base):
    __tablename__ = 'game'

    name = db.Column(db.String(144), nullable=False)
    developer = db.Column(db.String(144), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    reviews = db.relationship('Review', backref='game', lazy=True)
    categories = db.relationship('Category',
        secondary=game_category,
        back_populates='games'
    )

    def __init__(self, name, developer, year):
        self.name = name
        self.developer = developer
        self.year = year

    def find_reviews(self): 
        return self.reviews

    def find_average_score(game_id):
        stmt = text('SELECT AVG(rating) FROM review '
            'WHERE review.game_id = :game_id'
        ).params(game_id = game_id)

        res = db.engine.execute(stmt).first()[0]
        if (res):
            return round(res, 2)
    
    @staticmethod
    def find_highest_rated():
        stmt = text('SELECT game.name, AVG(review.rating) as avg_rating '
            'FROM game, review WHERE game.id = review.game_id '
            'GROUP BY game.name '
            'ORDER BY avg_rating DESC '
            'LIMIT 1')

        res = db.engine.execute(stmt).first()

        return {"name": res[0], "rating": round(res[1], 2)}
