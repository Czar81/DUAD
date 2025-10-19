from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from utils.api_exception import APIException

user_table = TablesManager.user_table
engine = TablesManager.engine


class DbUserManager:

    def insert_user(self, name: str, password: str, role: str):
        stmt = (
            insert(user_table)
            .returning(user_table.c.id)
            .values(name=name, password=password, role=role)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_user(
        self,
        id: int | None = None,
        name: str | None = None,
        password: str | None = None,
        role: str | None = None,
    ):
        params = filter_locals(
            locals(),
            (
                "self",
                "password",
            ),
        )
        conditions = []
        for key, value in params.items():
            if value is not None:
                conditions.append(getattr(user_table.c, key) == value)
        stmt = select(user_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt)
            return [dict(row) for row in result.mappings().all()]

    @classmethod
    def get_user_role_by_id(self, id):
        stmt = select(user_table.c.role).where(user_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result == None:
                raise APIException("Id not allowed", 404)
            role = result.scalar()
            return role

    def update_user(
        self,
        id: int,
        name: str | None = None,
        password: str | None = None,
        role: str | None = None,
    ):
        values = filter_locals(locals(), ("self", "id"))
        
        stmt = update(user_table).where(user_table.c.id == id)
        if values:
            stmt = stmt.values(**value)
        else:
            raise APIException("No provide any value", 400)
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
