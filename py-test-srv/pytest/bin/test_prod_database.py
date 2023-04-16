from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from .connection.prod import get_db, engine

def has_column(fld: str) -> bool:
    has_column = False
    insp = inspect(engine)
    for col in insp.get_columns('dog'):
        if fld not in col['name']:
            continue
        has_column = True
    return has_column

def test_prod_database_connecion():
    db: sessionmaker = next(get_db())
    assert db is not None

def test_prod_database_has_table():
    insp = inspect(engine)
    assert insp.has_table('dog')

def test_prod_database_has_id():
    assert has_column('id') == True

def test_prod_database_has_breed():
    assert has_column('breed') == True

def test_prod_database_has_color():
    assert has_column('color') == True