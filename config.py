import os

class Config:
    SECRET_KEY = 'wn1a3fncz2ayhapg2o1xznmuf'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'salim.nogorbekov@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'jamesfox23')