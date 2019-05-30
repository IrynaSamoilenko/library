import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:12345678@localhost/library"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'