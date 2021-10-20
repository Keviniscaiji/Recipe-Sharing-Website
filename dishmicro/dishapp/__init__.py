from flask import Flask
from dishapp.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)
db = SQLAlchemy(app)

from dishapp import routes, models
