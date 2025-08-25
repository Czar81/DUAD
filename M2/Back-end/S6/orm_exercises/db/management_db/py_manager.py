from sqlalchemy import create_engine
from sqlalchemy import insert, update
from sqlalchemy import delete


engine = None


def instantiate_engine(db_url):
    global engine
    engine = create_engine(db_url, echo=True)


def insert_table(user_table, name):
    stmt = insert(user_table).values(name=name)
    with engine.connect() as connection:
        result = connection.execute(stmt)  # What this return?
        connection.commit()


def update_table(user_table, id, name):
    stmt = update(user_table).where(user_table.c.id == id).values(name=name)
    with engine.connect() as connection:
        result = connection.execute(stmt)
        connection.commit()


def delete_table(user_table, id):
    stmt = delete(user_table).where(user_table.c.id == id)
    with engine.connect() as connection:
        result = connection.execute(stmt)
        connection.commit()
