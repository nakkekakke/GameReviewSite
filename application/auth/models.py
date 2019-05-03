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
    
    def favorite_category(self):
        stmt = text('SELECT category.name, '
            'AVG(review.rating) as avg_rating '
            'FROM category, gamecategory, game, review, account '
            'WHERE category.id = gamecategory.category_id '
            'AND gamecategory.game_id = game.id '
            'AND game.id = review.game_id '
            'AND review.account_id = account.id '
            'AND account.id = :account_id ' 
            'GROUP BY category.name ORDER BY avg_rating DESC '
            'LIMIT 1').params(account_id = self.id)
        
        res = db.engine.execute(stmt).first()

        return {"name": res[0], "rating": round(res[1], 2)}




