from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import _filter_locals, _filter_values
from utils.api_exception import APIException

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
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_data(
        self,
        id: int | None = None,
        name: str | None = None,
        password: str | None = None,
        role: str | None = None,
    ):
        conditions = _filter_locals(
            user_table,
            locals(),
            (
                "self",
                "password",
            ),
        )
        stmt = select(user_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt)
            return [dict(row) for row in result.mappings().all()]

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
        values= _filter_values(locals(), ("self", "id"))
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

    def delete_data(self, id_user: int):
        stmt = delete(user_table).where(user_table.c.id == id_user)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"User id:{str(id_user)} not exist", 404)
            else:
                conn.commit()
