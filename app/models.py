from . import db
from sqlalchemy.sql import func


class User(db.Model):
    ___tablename__ ='users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'