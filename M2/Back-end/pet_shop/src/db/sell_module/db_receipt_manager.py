from sqlalchemy import select, insert, update, and_, Table
from src.utils.api_exception import APIException
from datetime import datetime
from src.db.utils_db.helpers import _filter_locals
from src.db.utils_db.verifies import (
    _verify_user_own_cart,
    _verify_user_own_address,
    _verify_user_own_payment,
)


class DbReceiptManager:
    def __init__(self, TablesManager):
        self.cart_item_table = TablesManager.cart_item_table
        self.receipt_table = TablesManager.receipt_table
        self.product_table = TablesManager.product_table
        self.engine = TablesManager.engine

    def create_receipt(
        self,
        id_cart: int,
        id_address: int,
        id_payment: int,
        state: str | None = None,
        id_user: int | None = None,
    ):
        with self.engine.connect() as conn:
            if state is None:
                state = "bought"
            if not _verify_user_own_cart(conn, id_user, id_cart=id_cart):
                raise APIException(
                    f"Cart id:{id_cart} not owned by user or not exist", 403
                )
            if not _verify_user_own_address(conn, id_address, id_user):
                raise APIException(
                    f"Address id:{id_address} not owned by user or not exist", 403
                )
            if not _verify_user_own_payment(conn, id_payment, id_user ):
                raise APIException(
                    f"Payment id:{id_payment} not owned by user or not exist", 403
                )
            stmt_product = (
                select(
                    self.cart_item_table.c.id_product,
                    self.cart_item_table.c.amount.label("amount_bought"),
                    self.product_table.c.amount.label("actual_amount"),
                )
                .select_from(self.cart_item_table)
                .join(
                    self.product_table,
                    self.product_table.c.id == self.cart_item_table.c.id_product,
                )
                .where(self.cart_item_table.c.id_cart == id_cart)
            )

            products = conn.execute(stmt_product).mappings().all()

            if not products:
                raise APIException(f"Cart id:{id_cart} not found or has no items", 404)
            products_with_stock = []
            for row in products:
                new_amount = row["actual_amount"] - row["amount_bought"]
                if new_amount < 0:
                    raise APIException(
                        f"Not enough products available: {row["actual_amount"]}, requested: {row['amount_bought']} for product id: {row['id_product']}",
                        400,
                    )
                products_with_stock.append((row["id_product"], new_amount))
            stmt_create = (
                insert(self.receipt_table)
                .returning(self.receipt_table.c.id)
                .values(
                    id_cart=id_cart,
                    id_address=id_address,
                    id_payment=id_payment,
                    state=state,
                )
            )
            id_new_receipt = conn.execute(stmt_create).scalar()
            for id_product, new_amount in products_with_stock:
                stmt_update_product = (
                    update(self.product_table)
                    .where(self.product_table.c.id == id_product)
                    .values(amount=new_amount)
                )
                conn.execute(stmt_update_product)
            if id_new_receipt is None:
                raise APIException("Could not create receipt", 500)
            conn.commit()
        return id_new_receipt

    def get_data(
        self,
        id: int | None = None,
        id_user: int | None = None,
        id_cart: int | None = None,
        id_address: int | None = None,
        id_payment: int | None = None,
        entry_date: str | None = None,
        state: str | None = None,
    ):
        conditions = _filter_locals(
            self.receipt_table,
            locals(),
            exclude=("self", "id_user",)
        )
        with self.engine.connect() as conn:
            if id_user is not None and id is not None:
                if not _verify_user_own_cart(
                    conn, id, id_user, table=self.receipt_table
                ):
                    raise APIException(f"Receipt id:{id} does not exist", 403)
            if entry_date is not None:
                self.__validate_date_str(entry_date)

            stmt = select(self.receipt_table)
            if conditions:
                stmt = stmt.where(and_(*conditions))
            result = conn.execute(stmt).mappings().all()
        if result:
            return [dict(row) for row in result]
        error_msg = (
            f"Receipt id:{id_receipt} not found"
            if id_receipt is not None
            else "No receipts found matching criteria"
        )
        raise APIException(error_msg, 404)

    def update_data(self, id: int, state: str, id_user: int | None = None):
        with self.engine.connect() as conn:
            stmt_get_cart_id=select(self.receipt_table.c.id_cart).where(self.receipt_table.c.id == id)
            id_cart=conn.execute(stmt_get_cart_id).scalar()
            if not _verify_user_own_cart(conn, id_user, id_cart=id_cart):
                raise APIException(
                    f"Cart id:{id} not owned by user or not exist", 403
                )
            stmt = (
                update(self.receipt_table)
                .where(self.receipt_table.c.id == id)
                .values(state=state)
            )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Receipt id:{id} not exist", 404)
            conn.commit()
        return True

    def return_receipt(self, id: int, id_user: int):
        with self.engine.connect() as conn:
            if not _verify_user_own_cart(
                conn, id_user, id, table=self.receipt_table
            ):
                raise APIException(
                    f"Receipt id:{id} not owned by user or not exist", 403
                )
            stmt_join = (
                select(
                    self.cart_item_table.c.id_product,
                    self.cart_item_table.c.amount.label("amount_bought"),
                    self.product_table.c.amount.label("actual_amount"),
                    self.receipt_table.c.state,
                )
                .select_from(self.receipt_table)
                .join(
                    self.cart_item_table,
                    self.receipt_table.c.id_cart == self.cart_item_table.c.id_cart,
                )
                .join(
                    self.product_table,
                    self.product_table.c.id == self.cart_item_table.c.id_product,
                )
                .where(self.receipt_table.c.id == id)
            )
            products = conn.execute(stmt_join).mappings().all()
            if not products:
                raise APIException(
                    f"Receipt id:{id} not found or has no items", 404
                )
            if products[0]["state"] == "returned":
                raise APIException(f"Receipt id{id}, is already returned", 400)
            for row in products:
                new_amount = row["actual_amount"] + row["amount_bought"]
                stmt_update_product = (
                    update(self.product_table)
                    .where(self.product_table.c.id == row["id_product"])
                    .values(amount=new_amount)
                )
                conn.execute(stmt_update_product)
            stmt_update_receipt = (
                update(self.receipt_table)
                .where(self.receipt_table.c.id == id)
                .values(state="returned")
            )
            conn.execute(stmt_update_receipt)
            conn.commit()
        return True

    def __validate_date_str(self, date_str: str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise APIException("Entry date in receipt is not valid", 400)
