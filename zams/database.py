from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchmey.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeingKey

from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# make sure our models get created before we used them
from models import *

Base.metadata.create_all(engine)
