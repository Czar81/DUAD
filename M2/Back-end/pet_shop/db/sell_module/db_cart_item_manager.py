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
            if not _verify_user_own_cart(conn=conn, id_user=id_user, id_cart=id_cart):
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
        with engine.connect() as conn:
            if not _verify_user_own_cart(conn=conn, id_user=id_user, id_item=id_item, id_cart=id_cart, table=cart_item_table):
                raise APIException(f"Cart not owned by user id:{id_user}", 403)
            stmt = select(cart_item_table)
            if conditions:
                stmt = stmt.where(and_(*conditions))
            result = conn.execute(stmt).mappings().all()
            if result:
                return [dict(row) for row in result]
            raise APIException(f"Item cart id:{id_item} not exist",404)

    def update_data(
        self,
        id_item: int,
        amount: int,
        id_user: int | None = None,
    ):
        with engine.connect() as conn:
            if not _verify_user_own_cart(conn=conn, id_user=id_user, id_table=id_item, table=cart_item_table):
                raise APIException(f"Cart not owned by user id:{id_user}", 403)
            stmt = update(cart_item_table).where(cart_item_table.c.id_item == id_item).values(amount=amount)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException((f"Item id:{id_item} not exist"),404)
            conn.commit()

    def delete_data(self, id_item: int, id_user: int | None = None):
        with engine.connect() as conn:
            if not _verify_user_own_cart(conn=conn, id_user=id_user, id_table=id_item, table=cart_item_table):
                raise APIException(f"Cart not owned by user id:{id_user}", 403)
            stmt = delete(cart_item_table).where(cart_item_table.c.id == id_item)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Iteam id:{str(id_item)} not exist",404)
            conn.commit()
