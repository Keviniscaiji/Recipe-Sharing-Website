import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gkw001122'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, "dishapp.db")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    Avatar_UPLOAD_DIR = os.path.join(basedir,'static/uploaded_Avatar')
    DishPic_UPLOAD_DIR = os.path.join(basedir, 'static/dishes_pic')
