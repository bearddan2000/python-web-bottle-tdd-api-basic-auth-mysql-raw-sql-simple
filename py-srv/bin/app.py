import bottle
from bottle import auth_basic, route, run, request
from bottle.ext.sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from connection.prod import engine, session_local
from connection.api import get_db

from model import Base
from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

def setup_routes():
     bottle.route('/dog/<dog_id>', ['GET', 'DELETE'], crud)
     bottle.route('/dog/<dog_name>/<dog_color>', ['PUT'], insert_entry)
     bottle.route('/dog/<dog_id>/<dog_name>/<dog_color>', ['POST'], update_entry)
     
     # for api testing
     bottle.route('/api/dog', ['GET'], api_get_all)
     bottle.route('/api/dog/<dog_id>', ['GET', 'DELETE'], api_crud)
     bottle.route('/api/dog/<dog_name>/<dog_color>', ['PUT'], api_insert_entry)
     bottle.route('/api/dog/<dog_id>/<dog_name>/<dog_color>', ['POST'], api_update_entry)

def get_strategy(db):
     return Raw(db)

def is_authenticated_user(user, password):
    # You write this function. It must return
    # True if user/password is authenticated, or False to deny access.
	if user == 'user' and password == 'pass':
		return True
	return False

@route('/')
def hello():
	return {"hello": "world"}

@route('/api')
def api_hello():
	return {"hello": "world"}

@route('/dog')
@auth_basic(is_authenticated_user)
def get_all(db):
    strategy = get_strategy(db)
    return strategy.all()

@auth_basic(is_authenticated_user)
def api_get_all():
    db = next(get_db())
    strategy = get_strategy(db)
    return strategy.all()

@auth_basic(is_authenticated_user)
def crud(db, dog_id):
    strategy = get_strategy(db)
    if request.method == 'GET':
        return strategy.filter_by(dog_id)
    
    return strategy.delete_by(dog_id)

@auth_basic(is_authenticated_user)
def api_crud(dog_id):
    db = next(get_db())
    strategy = get_strategy(db)
    if request.method == 'GET':
        return strategy.filter_by(dog_id)
    
    return strategy.delete_by(dog_id)

@auth_basic(is_authenticated_user)
def insert_entry(db, dog_name, dog_color):
    strategy = get_strategy(db)
    return strategy.insert_entry(dog_name, dog_color)

@auth_basic(is_authenticated_user)
def api_insert_entry(dog_name, dog_color):
    db = next(get_db())
    strategy = get_strategy(db)
    return strategy.insert_entry(dog_name, dog_color)

@auth_basic(is_authenticated_user)
def update_entry(db, dog_id, dog_name, dog_color):
    strategy = get_strategy(db)
    return strategy.update_entry(dog_id, dog_name, dog_color)

@auth_basic(is_authenticated_user)
def api_update_entry(dog_id, dog_name, dog_color):
    db = next(get_db())
    strategy = get_strategy(db)
    return strategy.update_entry(dog_id, dog_name, dog_color)

bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=False, create_session = session_local))

setup_routes()

run(host='0.0.0.0', port=8000,debug=True)
