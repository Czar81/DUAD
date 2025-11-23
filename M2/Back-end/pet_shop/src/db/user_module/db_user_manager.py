from sqlalchemy import insert, select, delete, update, and_
from src.utils.helpers import filter_values
from src.utils.api_exception import APIException


class DbUserManager:

    def __init__(self, TablesManager):
        self.user_table = TablesManager.user_table
        self.engine = TablesManager.engine


    def insert_data(self, name: str, password: str, role: str):
        stmt = (
            insert(self.user_table)
            .returning(self.user_table.c.id)
            .values(name=name, password=password, role=role)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            if result is None:
                raise APIException("Could not create user", 500)
            conn.commit()
        return result

    def get_data(self, name: str, id_user: int):
        stmt = select(self.user_table).where(
            and_(self.user_table.c.name == name, self.user_table.c.id_user == id_user)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            return result
    
    def get_user(self, username, password):
        stmt = (
            select(self.user_table)
            .where(self.user_table.c.username == username)
            .where(self.user_table.c.password == password)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            return result
            
    def get_role_by_id(self, id):
        stmt = select(self.user_table.c.role).where(self.user_table.c.id == id)
        with self.engine.connect() as conn:
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
        stmt = update(self.user_table).where(self.user_table.c.id == id_user)
        if values:
            stmt = stmt.values(**values)
        else:
            raise APIException("No provide any value", 400)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"User id:{str(id_user)} not exist", 404)
            conn.commit()
        return True

    def delete_data(self, id_user: int):
        stmt = delete(self.user_table).where(self.user_table.c.id == id_user)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"User id:{str(id_user)} not exist", 404)
            else:
                conn.commit()
        return True

