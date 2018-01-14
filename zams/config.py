import os

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("ZAMS_DB_URI",
            "database://username:password@localhost:port/database")
    DEBUG = True
    SECRET_KEY = os.environ.get("ZAMS_SECRET_KEY", os.urandom(12))
