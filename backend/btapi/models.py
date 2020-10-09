"""
models.py
- Data classes for the surveyapi application
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import enum

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  books = db.relationship('Book', backref="creator", lazy=False)

  def __init__(self, email, password):
    self.email = email
    self.password = generate_password_hash(password, method='sha256')

  @classmethod
  def authenticate(cls, **kwargs):
    email = kwargs.get('email')
    password = kwargs.get('password')

    if not email or not password:
      return None
    
    user = cls.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
      return None

    return user

  def to_dict(self):
    return dict(id=self.id, email=self.email)

class Genre(enum.Enum):
  SCIFI = "Science Fiction"
  FANT = "Fantasy"
  NFICT = "Non-fiction"
  MYST = "Mystery"
  HOR = "Horror"
  SHELP = "Self Help"
  MEM = "Memoir"

class Book(db.Model):
  __tablename__ = 'books'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text)
  author = db.Column(db.Text)
  read = db.Column(db.Boolean, unique=False)
  genre = db.Column(db.Enum(Genre)) # troubleshooting-> https://stackoverflow.com/questions/36136112/defining-sqlalchemy-enum-column-with-python-enum-raises-valueerror-not-a-valid
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def to_dict(self):
    return dict(
      id = self.id,
      title = self.title,
      author = self.author,
      genre = self.genre,
      read = self.read,
      created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
    )