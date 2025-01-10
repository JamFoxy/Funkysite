import logging

from flask import Flask
from flask_mail import Mail
from config import Config
from app import routes

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail()
mail.init_app(app)


if not app.debug:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)
    app.logger.addHandler(stream_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Flask startup!')