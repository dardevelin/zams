import os

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "database://username:password@domain:port/database"
    DEBUG = True
    SECRET_KEY = os.environ.get("ZAMS_SECRET_KEY", os.urandom(12))

