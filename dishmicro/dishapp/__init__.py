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
# app.logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s-%(levelname)s: %(message)s')
# console_handler = logging.StreamHandler(sys.stdout)
# console_handler.formatter = formatter
# console_handler.setLevel(logging.DEBUG)
# app.logger.addHandler(console_handler)

# logfile = 'DEBUG.log'
# File_handler = logging.FileHandler(logfile, mode='a', encoding='utf8')
# File_handler.setFormatter(formatter)
# File_handler.setLevel(logging.DEBUG)
# app.logger.addHandler(File_handler)
# handler1 = logging.StreamHandler(sys.stdout)

handler1 = logging.FileHandler("logs/Error.log",mode="w")
formatter = logging.Formatter('%(asctime)s %(name)-s %(levelname)-s %(message)s')
handler1.setFormatter(formatter)
handler1.setLevel(logging.ERROR)
app.logger.addHandler(handler1)
#
handler2 = logging.FileHandler("logs/Debug.log",mode="w")
formatter = logging.Formatter('%(asctime)s %(name)-s %(levelname)-s %(message)s')
handler2.setFormatter(formatter)
handler2.setLevel(logging.DEBUG)
app.logger.addHandler(handler2)
#
handler3 = logging.FileHandler("logs/Info.log",mode="w")
formatter = logging.Formatter('%(asctime)s %(name)-s %(levelname)-s %(message)s')
handler3.setFormatter(formatter)
handler3.setLevel(logging.INFO)
app.logger.addHandler(handler3)

app.logger.info("Example info")
app.logger.error("Example error")