"""
api.py
- provides the API endpoints for consuming and producing 
  REST requests and responses
"""

from functools import wraps
from datetime import datetime, timedelta

from flask import Blueprint, request, jsonify, current_app

import jwt

from .models import db, Book, User

api = Blueprint('api', __name__)

def token_required(f):
  @wraps(f)
  def _verify(*args, **kwargs):
    auth_headers = request.headers.get('Authorization', '').split()

    print(auth_headers)

    invalid_msg = {
      'message': 'Invalid token. Registration and/or authentication required',
      'authenticated': False
    }
    expired_msg = {
      'message': 'Expired token. Reauthentication required',
      'authenticated': False
    }

    if len(auth_headers) != 2:
      return jsonify(invalid_msg), 401

    try:
      token = auth_headers[1]
      data = jwt.decode(token, current_app.config['SECRET_KEY'])
      user = User.query.filter_by(email=data['sub']).first()
      if not user:
        raise RuntimeError('User not found')
      return f(user, *args, **kwargs)
    except jwt.ExpiredSignatureError:
      return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
    except (jwt.InvalidTokenError, Exception) as e:
      print(e)
      return jsonify(invalid_msg), 401
  return _verify

# Sign Up Functionality to create a new user
@api.route('/register/', methods=('POST',))
def register():
  data = request.get_json()
  user = User(**data)
  db.session.add(user)
  db.session.commit()
  return jsonify(user.to_dict()), 201

@api.route('/login/', methods=('POST',))
def login():
  data = request.get_json()
  user = User.authenticate(**data)

  if not user:
    return jsonify({ 'message': 'Invalid credentials', 'authenticated': False }), 401

  token = jwt.encode({
    'sub': user.email,
    'iat': datetime.utcnow(),
    'exp': datetime.utcnow() + timedelta(minutes=30)
    },
    current_app.config['SECRET_KEY']
  )
  return jsonify({'token': token.decode('UTF-8')})

@api.route('/hello/<string:name>/')
def say_hello(name):
  response = { 'msg': "Hello {}".format(name) }
  return response

@api.route('/books/', methods=('POST',))
def create_book(current_user):
    data = request.get_json()
    book = Book(
      title=data['title'], 
      author=data['author'],
      read=data['read'],
      genre=data['genre'])
    book.creator = current_user
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

# Need to filter for just current user's books eventually
@api.route('/books/', methods=('GET',))
def fetch_books():
    books = Book.query.all()
    return jsonify([s.to_dict() for s in books])