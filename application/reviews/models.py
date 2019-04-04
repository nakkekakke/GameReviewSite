from application import db
from application.models import Base

class Review(Base):
    __tablename__ = 'review'

    content = db.Column(db.String(144), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    game_id = db.Column(db.Integer,
        db.ForeignKey('game.id'),
        nullable=False
    )
    account_id = db.Column(db.Integer,
        db.ForeignKey('account.id'),
        nullable=False
    )

    def __init__(self, content, rating):
        self.content = content
        self.rating = rating