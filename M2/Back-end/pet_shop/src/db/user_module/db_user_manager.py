from sqlalchemy import insert, select, delete, update, and_
from src.utils.helpers import filter_values
from src.utils.api_exception import APIException
from src.db.utils_db.tables_manager import TablesManager

user_table = TablesManager.user_table
engine = TablesManager.engine

class DbUserManager:


    def insert_data(self, name: str, password: str, role: str):
        stmt = (
            insert(user_table)
            .returning(user_table.c.id)
            .values(name=name, password=password, role=role)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            if result is None:
                raise APIException("Could not create user", 500)
            conn.commit()
        return result

    def get_data(self, name: str, id_user: int):
        stmt = select(user_table).where(
            and_(user_table.c.name == name, user_table.c.id_user == id_user)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            return result
    
    def get_user(self, username, password):
        stmt = (
            select(user_table)
            .where(user_table.c.username == username)
            .where(user_table.c.password == password)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            return result
            
    @classmethod
    def get_role_by_id(self, id):
        stmt = select(user_table.c.role).where(user_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
        if result == None:
            raise APIException("Id not allowed", 404)
        role = result.scalar()
        return role

    def update_data(
        self,
        id_user: int,
        name: str | None = None,
        password: str | None = None,
        role: str | None = None,
    ):
        values = filter_values(locals(), ("self", "id_user"))
        stmt = update(user_table).where(user_table.c.id == id_user)
        if values:
            stmt = stmt.values(**values)
        else:
            raise APIException("No provide any value", 400)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"User id:{str(id_user)} not exist", 404)
            conn.commit()
        return True

    def delete_data(self, id_user: int):
        stmt = delete(user_table).where(user_table.c.id == id_user)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"User id:{str(id_user)} not exist", 404)
            else:
                conn.commit()
        return True

