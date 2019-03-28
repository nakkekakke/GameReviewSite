from application import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,
        default=db.func.current_timestamp()
    )
    date_modified = db.Column(db.DateTime,
        default=db.func.current_timestamp(),
        onupdate = db.func.current_timestamp()
    )
    name = db.Column(db.String(144), nullable=False)
    developer = db.Column(db.String(144), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(144))

    def __init__(self, name, developer, year, genre):
        self.name = name
        self.developer = developer
        self.year = year
        self.genre = genre
