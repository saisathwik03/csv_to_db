import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/databasetocsv'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
