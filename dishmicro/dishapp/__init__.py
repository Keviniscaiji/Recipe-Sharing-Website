import sys

from flask import Flask
from dishapp.config import Config
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)
db = SQLAlchemy(app)


from dishapp import routes, models

# import logging
app.logger = logging.getLogger()

# add the handler for Error and create a log file
handler1 = logging.FileHandler("logs/Error.log",mode="a")
formatter = logging.Formatter('%(asctime)s %(name)-s %(levelname)-s %(message)s')
handler1.setFormatter(formatter)
handler1.setLevel(logging.ERROR)
app.logger.addHandler(handler1)
# add the handler for Debug and create a log file
handler2 = logging.FileHandler("logs/Debug.log",mode="a")
formatter = logging.Formatter('%(asctime)s %(name)-s %(levelname)-s %(message)s')
handler2.setFormatter(formatter)
handler2.setLevel(logging.DEBUG)
app.logger.addHandler(handler2)
# add the handler for Info and create a log file
handler3 = logging.FileHandler("logs/Info.log",mode="a")
formatter = logging.Formatter('%(asctime)s %(name)-s %(levelname)-s %(message)s')
handler3.setFormatter(formatter)
handler3.setLevel(logging.INFO)
app.logger.addHandler(handler3)

app.logger.info("Example info")
app.logger.error("Example error")