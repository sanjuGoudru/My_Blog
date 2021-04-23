# -*- coding: utf-8 -*-
import os


class Config:
    SECRET_KEY = os.environ.get('MY_FLASK_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('MY_FLASK_SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
