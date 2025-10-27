from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import _filter_locals, _verify_user_own_cart
from utils.api_exception import APIException

cart_item_table = TablesManager.cart_item_table
engine = TablesManager.engine


class DbCartItemsManager:

    def insert_data(self, id_cart: int, id_product: int, amount: int, id_user: int | None = None):
        stmt = (
            insert(cart_item_table)
            .returning(cart_item_table.c.id)
            .values(id_cart=id_cart, id_product=id_product, amount=amount)
        )
        with engine.connect() as conn:
            if id_user is not None and not _verify_user_own_cart(
                conn, id_cart, id_user, cart_item_table
            ):
                raise APIException(f"Cart id:{id_cart} not owned by user id:{id_user}", 403)
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_data(
        self,
        id_item: int | None = None,
        id_user: int | None = None,
        id_cart: int | None = None,
        id_product: int | None = None,
        amount: int | None = None,
    ):
        conditions = _filter_locals(cart_item_table,locals())
        stmt = select(cart_item_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            if id_user is not None and not _verify_user_own_cart(
                conn, id_item, id_user, cart_item_table
            ):
                raise APIException(f"Item id:{id_item} not owned by user id:{id_user}", 403)
            result = conn.execute(stmt).mappings().all()
            if result:
                return [dict(row) for row in result]

            raise APIException(
                (
                    f"Item cart id:{str(id_item)} not exist or not in the cart"
                    if id_cart
                    else f"Item cart id:{str(id_item)} not exist"
                ),
                404,
            )

    def update_data(
        self,
        id_item: int,
        amount: int,
        id_user: int | None = None,
        id_cart: int | None = None,
    ):
        conditions = [cart_item_table.c.id == id_item]

        if id_cart is not None:
            conditions.append(cart_item_table.c.id_cart == id_cart)
        with engine.connect() as conn:
            if id_user is not None and not _verify_user_own_cart(
                conn, id_user, id_cart
            ):
                raise APIException(f"Cart id:{id_cart} not owned by user id:{id_user}", 403)
            stmt = (
                update(cart_item_table).where(and_(*conditions)).values(amount=amount)
            )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(
                    (
                        f"Item id:{id_item} not exist or not owned by cart id:{id_cart}"
                        if id_cart
                        else f"Item id:{id_item} not exist"
                    ),
                    404,
                )
            conn.commit()

    def delete_data(
        self, id_item: int, id_user: int | None = None, id_cart: int | None = None
    ):
        conditions = [cart_item_table.c.id == id_item]
        if id_cart:
            conditions.append(cart_item_table.c.id_cart == id_cart)
        with engine.connect() as conn:
            if id_user is not None and not _verify_user_own_cart(
                conn, id_item, id_user, cart_item_table
            ):
                raise APIException(f"Item id:{id_item} not owned by user id:{id_user}", 403)
            stmt = delete(cart_item_table).where(and_(*conditions))
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(
                    (
                        f"Iteam id:{str(id_item)} not exist or not owned by cart id:{id_cart}"
                        if id_cart
                        else f"Iteam id:{str(id_item)} not exist"
                    ),
                    404,
                )
            conn.commit()
