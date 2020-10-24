from . import db
from sqlalchemy.sql import func
from . import login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    ___tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'