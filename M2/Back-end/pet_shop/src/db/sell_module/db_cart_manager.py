from sqlalchemy import insert, select, delete, update, and_
from src.db.utils_db.helpers import _filter_locals
from src.db.utils_db.verifies import _verify_user_own_cart
from src.utils.api_exception import APIException


class DbCartManager:
    def __init__(self, TablesManager):
        self.cart_table = TablesManager.cart_table
        self.engine = TablesManager.engine

    def insert_data(self, id_user: int, state: str | None = None):
        with self.engine.connect() as conn:
            values = {"id_user": id_user}
            if not self.__verify_if_cart_is_active(conn, id_user) and (
                state == "active" or state is None
            ):
                raise APIException(
                    f"User id: {id_user} already have an active cart", 400
                )
            if state is not None:
                values["state"] = state
            stmt = (
                insert(self.cart_table).returning(self.cart_table.c.id).values(**values)
            )
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_data(
        self,
        id: int | None = None,
        id_user: int | None = None,
        state: str | None = None,
    ):
        conditions = _filter_locals(
            self.cart_table,
            locals(),
            (
                "self",
                "id",
            ),
        )
        with self.engine.connect() as conn:
            if not _verify_user_own_cart(conn, id_user, id_cart):
                raise APIException(f"Cart id:{id_cart} not exist", 401)
            result = conn.execute(stmt).mappings().all()
            if result:
                return [dict(row) for row in result]
            raise APIException(f"Cart id:{id_item} not exist", 404)

    def update_data(self, id_cart: int, state: str, id_user: int | None = None):
        with self.engine.connect() as conn:
            if not _verify_user_own_cart(conn, id_user, id_cart):
                raise APIException(f"Cart id:{id_cart} not exist", 401)
            if self.__verify_if_cart_is_active(conn, id_user) and state == "active":
                raise APIException(
                    f"User id: {id_user} already has an active cart", 400
                )
            stmt_select = select(self.cart_table.c.id).where(
                self.cart_table.c.id_user == id_user,
                self.cart_table.c.state == "active",
            )
            id_active_cart = conn.execute(stmt_select)
            stmt_update_old = (
                update(self.cart_table)
                .where(self.cart_table.c.id == id_active_cart)
                .values(state="inactive")
            )
            conn.execute(stmt_update_old)
            stmt = (
                update(self.cart_table)
                .where(self.cart_table.c.id == id_cart)
                .values(state=state)
            )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Cart id:{str(id_cart)} does not exist", 404)
            conn.commit()

    def delete_data(self, id_cart: int, id_user: int | None = None):
        stmt = delete(self.cart_table).where(self.cart_table.c.id == id_cart)
        with self.engine.connect() as conn:
            if id_user is not None:
                if not _verify_user_own_cart(
                    conn=conn, id_user=id_user, id_cart=id_cart
                ):
                    raise APIException(f"Cart id:{id_cart} not exist", 401)
            if __verify_if_cart_is_active(id_user):
                raise APIException(
                    f"Cart id:{id_cart} is active, can not delete an active cart"
                )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Cart id:{id_cart} not exist", 404)
            conn.commit()

    def __verify_if_cart_is_active(self, conn, id_user: int | None):
        if id_user is None:
            return False
        stmt = select(self.cart_table).where(
            and_(
                self.cart_table.c.id_user == id_user,
                self.cart_table.c.state == "active",
            )
        )
        result = conn.execute(stmt).fetchall()
        return bool(result)
