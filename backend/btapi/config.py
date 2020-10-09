"""
config.py
- settings for the flask application object
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
  DEBUG = True
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-hidden-key'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'postgresql://boodoo:pass1234@localhost/books'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
