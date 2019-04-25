from application import db
from application.models import Base
from application.games.models import game_category

class Category(Base):
    __tablename__ = 'category'

    name = db.Column(db.String(144), nullable=False)

    games = db.relationship('Game',
        secondary=game_category,
        back_populates='categories'
    )

    def __init__(self, name):
        self.name = name
    