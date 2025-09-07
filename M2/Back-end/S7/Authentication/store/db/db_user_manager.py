from sqlalchemy import insert, select
from tables_metadata import TablesManager

user_table = TablesManager
engine = TablesManager.engine


class DbUserManager:

    def insert_user(self, username, password):
        stmt = (
            insert(user_table)
            .returning(user_table.c.id)
            .values(username=username, password=password)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_user(self, username, password):
        stmt = (
            select(user_table)
            .where(user_table.c.username == username)
            .where(user_table.c.password == password)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()

            if len(users) == 0:
                return None
            else:
                return users[0]

    def get_user_by_id(self, id):
        stmt = select(user_table).where(user_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if len(users) == 0:
                return None
            else:
                return users[0]
