from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import filter_locals 
from utils.api_exception import APIException

cart_table = TablesManager.cart_table
engine = TablesManager.engine


class DbCartManager:

    def insert(self, id_user: int, state: str | None = None):
        values = {"id_user": id_user}
        if self.__verify_if_cart_is_active(id_user):
            raise APIException(f"User id: {id_user} already have an active cart", 400)
        if state is not None:
            values["state"] = state
        stmt = insert(cart_table).returning(cart_table.c.id).values(**values)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()
        
    def get(self, id: int | None = None, id_user: int | None = None, state: str | None = None):
        params = filter_locals(locals(), ("self","id",))
        conditions = []
        for key, value in params.items():
            if value is not None:
                conditions.append(getattr(cart_table.c, key) == value)
        stmt = select(cart_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            return result

    def update(self, id: int, state: str, id_user: int | None = None):
        conditions = [cart_table.c.id == id]
        if __verify_if_cart_is_active(id_user) is not None:
            raise APIException(f"User id: {id_user} already have an active cart", 400)
        if id_user is not None:
            conditions.append(cart_table.c.id_user == id_user)
        stmt = update(cart_table).where(*conditions).values(state=state)
        #Agregar una verificacion  para que siempre haya solo uno en active
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated == 0:
                raise APIException(
                    (
                        f"Cart id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Cart id:{str(id)} not exist"
                    ),
                    404,
                )
            conn.commit()

    def delete(self, id: int, id_user: int | None = None):
        conditions = [cart_table.c.id == id]
        if id_user is not None:
            conditions.append(cart_table.c.id_user == id_user)
        stmt = delete(cart_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(
                    (
                        f"Cart id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Cart id:{str(id)} not exist"
                    ),
                    404,
                )
            conn.commit()

    def __verify_if_cart_is_active(self, id_user: int):
        stmt=select(cart_table).where(and_(cart_table.c.id_user==id_user, cart_table.c.state=="active"))
        with engine.connect() as conn:
            result = conn.execute(stmt).fetchall()
        return bool(result)