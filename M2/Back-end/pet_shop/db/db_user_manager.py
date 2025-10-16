from sqlalchemy import insert, select, delete, update
from .tables_manager import TablesManager
from utils.api_exception import APIException

user_table = TablesManager.user_table
engine = TablesManager.engine


class DbUserManager:

    def insert_user(self, name: str, password: str):
        stmt = (
            insert(user_table)
            .returning(user_table.c.id)
            .values(name=name, password=password)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_user(self, name, password):
        stmt = (
            select(user_table)
            .where(user_table.c.name == name)
            .where(user_table.c.password == password)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            return result

    @classmethod
    def get_user_role_by_id(self, id):
        stmt = select(user_table.c.role).where(user_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result == None:
                raise APIException("Id not allowed", 404)
            role = result.scalar()
            return role

    @classmethod
    def get_user_by_id(self, id):
        stmt = select(user_table).where(user_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if len(users) == 0:
                raise APIException(f"User with id:{id} not exist", 404)
            else:
                return users[0]

    def update_user(self, id: int, name: str, password: str, role: str):
        stmt = (
            update(user_table)
            .where(user_table.c.id == id)
            .values(name=name, password=password, role=role)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(f"User id:{str(id)} not exist", 404)
            else:
                conn.commit()

    def delete_user(self, id: int):
        stmt = delete(user_table).where(user_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(f"User id:{str(id)} not exist", 404)
            else:
                conn.commit()
