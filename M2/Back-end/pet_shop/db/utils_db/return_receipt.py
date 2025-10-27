from sqlalchemy import select, update, and_, Table
from utils.api_exception import APIException
from .tables_manager import TablesManager

cart_items_table = TablesManager.cart_items_table
cart_table = TablesManager.cart_table
receipt_table = TablesManager.receipt_table
product_table = TablesManager.product_table
engine = TablesManager.engine


class BuyManager:
    def return_receipt(self, id_receipt: int, id_user: int):
        with engine.connect() as conn:
            # Join cart with receipt
            join_cart_receipt = __dinamic_join(
                conn=conn,
                returning=(receipt_table),
                left_table=receipt_table,
                right_table=cart_table,
                join_condition=receipt_table.c.id_cart == cart_table.c.id,
                *[receipt_table.c.id == id_receipt, cart_table.c.id_user == id_user],
            )
            # Verify Receipt exist or user own it
            if not join_cart_receipt:
                raise APIException(
                    f"Receipt id:{id_receipt} not exist or not own by user id:{id_user}"
                )
            # Verify receipt is not already return
            if join_cart_receipt[0]["state"] == "return":
                raise APIException(f"Receipt id{id_receipt}, its already return", 400)
            # revisar join para obtener los products de una, tal vez con join_cart_receipt[0]["id_cart"]
            join_cart_items_cart_products = __dinamic_join(
                conn=conn,
                returning=(),
                right_table=cart_table,
                left_table=receipt_table,
                join_condition= "",
                *[]
            )
            #Make a for to update products with restore stock
            # Usar una clasee nueva para compras
            # Actualizar estado de receipt y ver como manejar cart.state

    def __dinamic_select(self, conn, table, condition=None):
        # Borrar si no se usa, preferiblement solo hacer un join
        stmt = select(table).where(condition)
        result = conn.execute(stmt).mappings().all()
        return result

    def __dinamic_join(
        self,
        conn,
        returning: tuple,
        left_table: Table,
        right_table: Table,
        join_condition,
        *conditions: tuple,
    ):
        stmt = select(returning).select_from(
            left_table.join(right_table, join_condition)
        )
        if conditions:
            stmt = stmt.where(and_(*conditions))
        result = conn.execute(stmt).mappings().all()
        return result
