from sqlalchemy import create_engine
import os
import urllib

class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bassrobert:180105Utl!@127.0.0.1/idgs801'
    SQLALCHEMY_TRACK_MODIFICATION = False