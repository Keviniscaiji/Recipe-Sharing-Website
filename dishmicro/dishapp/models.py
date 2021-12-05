from enum import unique
from datetime import datetime

from flask_wtf.file import FileRequired
from flask_wtf.form import FlaskForm

from sqlalchemy.orm import backref
from wtforms.fields.core import StringField, RadioField, DateField
from wtforms.fields.simple import SubmitField, FileField
from wtforms.validators import DataRequired
from dishapp import db
# form is from week 7 page 14
# the form that used to store user's basic information
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    profile = db.relationship('Profile', backref='user', lazy='dynamic')
    def __repr__(self):
        return 'User {}'.format(self.username)

# use the idea from week8 page 11-12 and make quite a big change to meet new requirements
# the form that used to store user's additional information
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dob = db.Column(db.DateTime, index=True)
    gender = db.Column(db.String(10), index=True)
    country = db.Column(db.String(20), index=True)
    avatar = db.Column(db.String(256), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Profile for user: {}, gender: {}, birthday: {}>'.format(self.user_id, self.dob, self.dob)
# part of the form are form week 7 page 14
# the form that used to store user's posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(10000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    dish_pic = db.Column(db.String(256), index=True, default="dish_default.jpeg")
    likes = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Post made on {}: {}>'.format(self.timestamp, self.body)




