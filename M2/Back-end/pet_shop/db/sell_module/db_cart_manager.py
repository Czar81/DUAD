from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import _filter_locals, _verify_user_own_cart
from utils.api_exception import APIException

cart_table = TablesManager.cart_table
engine = TablesManager.engine


class DbCartManager:

    def insert_data(self, id_user: int, state: str | None = None):
        values = {"id_user": id_user}
        if self.__verify_if_cart_is_active(id_user) and (state=="active"or state is None):
            raise APIException(f"User id: {id_user} already have an active cart", 400)
        if state is not None:
            values["state"] = state
        stmt = insert(cart_table).returning(cart_table.c.id).values(**values)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()
        
    def get_data(self, id: int | None = None, id_user: int | None = None, state: str | None = None):
        conditions = _filter_locals(cart_table,locals(), ("self","id",))
        stmt = select(cart_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            return result

    def update_data(self, id_cart: int, state: str, id_user: int | None = None):
        conditions = [cart_table.c.id == id_cart]
        with engine.connect() as conn:
            if id_user is not None:
                conditions.append(cart_table.c.id_user == id_user)
                if not _verify_user_own_cart(conn,id_cart, id_user):
                    raise APIException(f"User id:{id_user} does not own cart id:{id_cart}", 401)
                if self.__verify_if_cart_is_active(id_user) and state == "active":
                    raise APIException(f"User id: {id_user} already has an active cart", 400)
            stmt = update(cart_table).where(and_(*conditions)).values(state=state)
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated == 0:
                raise APIException(f"Cart id:{str(id_cart)} does not exist",404)
            conn.commit()

    def delete_data(self, id_cart: int, id_user: int | None = None):
        conditions = [cart_table.c.id == id_cart]
        if id_user is not None:
            conditions.append(cart_table.c.id_user == id_user)
        stmt = delete(cart_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException((f"Cart id:{str(id_cart)} not exist"),404)
            conn.commit()

    def __verify_if_cart_is_active(self, id_user: int):
        stmt=select(cart_table).where(and_(cart_table.c.id_user==id_user, cart_table.c.state=="active"))
        with engine.connect() as conn:
            result = conn.execute(stmt).fetchall()
        return bool(result)