from sqlalchemy import insert, select, delete, update, and_
from src.db.utils_db.helpers import _filter_locals
from src.db.utils_db.verifies import _verify_user_own_cart
from src.utils.api_exception import APIException


class DbCartManager:
    def __init__(self, TablesManager):
        self.cart_table = TablesManager.cart_table
        self.engine = TablesManager.engine

    def insert_data(self, id_user: int):
        values = {"id_user": id_user}
        with self.engine.connect() as conn:
            if self.__verify_if_cart_is_active(conn, id_user):
                values["state"] = "inactive"

            stmt = (
                insert(self.cart_table).returning(self.cart_table.c.id).values(**values)
            )
            result = conn.execute(stmt).scalar()
            if result is None:
                raise APIException("Could not create cart", 500)
            conn.commit()
        return result

    def get_data(
        self,
        id_user: int,
        id_cart: int | None = None,
        state: str | None = None,
    ):
        conditions = _filter_locals(self.cart_table, locals())
        stmt = select(self.cart_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with self.engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            if not result:
                return "Not carts found"
            return [dict(row) for row in result]

    def get_active_cart(
        self,
        id_user: int,
    ):
        stmt = select(self.cart_table).where(and_(self.cart_table.c.id==id_user, self.cart_table.c.state=="active"))
        with self.engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            if not result:
                raise APIException("Unexpected error occuerd trying to get current cart", 500)
            return [dict(row) for row in result]

    def update_data(self, id_cart: int, state: str, id_user: int):
        with self.engine.connect() as conn:
            if not _verify_user_own_cart(conn, id_user, id_cart=id_cart):
                raise APIException(f"Cart id:{id_cart} not exist", 401)

            stmt_select = select(self.cart_table).where(
                and_(
                    self.cart_table.c.id_user == id_user,
                    self.cart_table.c.state == "active",
                )
            )
            id_active_cart = conn.execute(stmt_select).scalar()
            if id_active_cart is not None:
                stmt_update_old = (
                    update(self.cart_table)
                    .where(self.cart_table.c.id == id_active_cart)
                    .values(state="inactive")
                )
                updated_old_cart = conn.execute(stmt_update_old)
            if updated_old_cart is None: 
                raise APIException(f"Must have another cart, can not have all unactive carts", 400)
            stmt = (
                update(self.cart_table)
                .where(self.cart_table.c.id == id_cart)
                .values(state=state)
            )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Cart id:{str(id_cart)} does not exist", 404)
            conn.commit()
        return True

    def delete_data(self, id_cart: int, id_user: int | None = None):
        stmt = delete(self.cart_table).where(self.cart_table.c.id == id_cart)
        with self.engine.connect() as conn:
            if id_user is not None:
                if not _verify_user_own_cart(
                    conn=conn, id_user=id_user, id_cart=id_cart
                ):
                    raise APIException(f"Cart id:{id_cart} not exist", 401)
            if self.__verify_if_cart_is_active(id_user):
                raise APIException(
                    f"Cart id:{id_cart} is active, can not delete an active cart"
                )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Cart id:{id_cart} not exist", 404)
            conn.commit()
        return True

    def __verify_if_cart_is_active(self, conn, id_user: int | None = None):
        if id_user is None:
            return False
        stmt = select(self.cart_table).where(
            and_(
                self.cart_table.c.id_user == id_user,
                self.cart_table.c.state == "active",
            )
        )
        result = conn.execute(stmt).fetchone()
        return bool(result)
