from sqlalchemy import insert, select, delete, update
from .tables_manager import TablesManager
from utils.api_exception import APIException
from utils.helpers import filter_locals 

cart_item_table = TablesManager.cart_item_table
engine = TablesManager.engine


class DbCartItemsManager:

    def add_cart_item(self, id_cart: int, id_product: int, amount: int):
        stmt = (
            insert(cart_item_table)
            .returning(cart_item_table.c.id)
            .values(id_cart=id_cart, id_product=id_product, amount=amount)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_cart_item(
        self,
        id: int | None = None,
        id_cart: int | None = None,
        id_product: int | None = None,
        amount: int | None = None,
    ):
        params = filter_locals(locals())

        conditions = []
        for key, value in params.items():
            if value is not None:
                conditions.append(getattr(cart_item_table.c, key) == value)
        stmt = select(cart_item_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            if result is not None:
                return [dict(row) for row in result.mappings().all()]
            raise APIException(
                (
                    f"Item cart id:{str(id)} not exist or not in the cart"
                    if id_cart
                    else f"Item cart id:{str(id)} not exist"
                ),
                404,
            )

    def update_cart_item(self, id: int, amount: int, id_cart: int | None = None):
        # Agregar join para verificar que el cart sea del user 
        conditions = [cart_item_table.c.id == id]
        if id_cart is not None:
            conditions.append(cart_item_table.c.id_cart == id_cart)
        stmt = update(cart_item_table).where(*conditions).values(amount=amount)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated != 0:
                conn.commit()

            raise APIException(
                (
                    f"Iteam id:{str(id)} not exist or not owned by user id:{id_cart}"
                    if id_cart
                    else f"Iteam id:{str(id)} not exist"
                ),
                404,
            )

    def delete_cart_item(self, id: int, id_user: str | None = None):
        # Agregar join para verificar que el cart sea del user 
        conditions = [cart_item_table.c.id == id]
        if id_user is not None:
            conditions.append(cart_item_table.c.id_user == id_user)
        stmt = delete(cart_item_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted != 0:
                conn.commit()

            raise APIException(
                (
                    f"Iteam id:{str(id)} not exist or not owned by user id:{id_cart}"
                    if id_cart
                    else f"Iteam id:{str(id)} not exist"
                ),
                404,
            )
