from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    pass_word= db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_word = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_word,password)


    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__='pitches'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id= db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    details= db.Column(db.String(), index=True)
    category = db.Column(db.String(255), nullable=False)
    
    @classmethod
    def getPitches(cls, id):
        pitches = Pitch.query.order_by(pitchId=id).desc().all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.details}'
