from sqlalchemy import insert, select, delete, update
from .tables_manager import TablesManager
from utils.api_exception import APIException

cart_item_table = TablesManager.cart_item_table
engine = TablesManager.engine


class DbCartItemsManager:
    def add_cart_item(self, id_user: int, id_cart: int, id_product: int, amount: int):
        stmt = (
            insert(cart_item_table)
            .returning(cart_item_table.c.id)
            .values(
                id_user=id_user, id_cart=id_cart, id_product=id_product, amount=amount
            )
        )

        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_cart_item(self, id: int | None = None, id_user: int | None = None):
        conditions = []
        if id is not None:
            conditions.append(cart_item_table.c.id == id)
        if id_user is not None:
            conditions.append(cart_item_table.c.id_user == id_user)

        stmt = select(cart_item_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            if result is not None:
                return [dict(row) for row in result.mappings().all()]
            else:
                raise APIException(f"User id:{str(id)} does not have any address", 404)


    def update_cart_item(self, id: int, id_user: int, amount: int):
        stmt = (
            update(cart_item_table)
            .where(cart_item_table.c.id == id, cart_item_table.c.id_user == id_user)
            .values(amount=amount)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated == 0:
                raise APIException(
                    f"Item id:{str(id)} not exist or not in the cart of user id:{id_user}",
                    404,
                )
            else:
                conn.commit()

    def delete_cart_item(self, id: int, id_user):
        stmt = delete(cart_item_table).where(
            cart_item_table.c.id == id, cart_item_table.c.id_user == id_user
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(
                    f"Item id:{str(id)} not exist or not in the cart of user id:{id_user}",
                    404,
                )
            else:
                conn.commit()
