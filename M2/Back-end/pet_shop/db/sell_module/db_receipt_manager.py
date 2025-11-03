from sqlalchemy import select, update, and_, Table
from utils.api_exception import APIException
from .tables_manager import TablesManager
from db.utils_db.helpers import _verify_user_own_cart

cart_items_table = TablesManager.cart_items_table
receipt_table = TablesManager.receipt_table
product_table = TablesManager.product_table

engine = TablesManager.engine


class DbReceiptManager:
    def create_receipt():
        pass

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
        filters = _filter_locals(
            receipt_table,
            locals(),
            (
                "self",
                "id_user",
            ),
        )
        conditions = []
        with engine.connect() as conn:
            if id_user is not None and id is not None:
                if not _verify_user_own_cart(conn, id, id_user, receipt_table):
                    raise APIException(f"Receipt id:{id} does not exist", 403)
            if entry_date is not None:
                self.__validate_date_str(entry_date)
            for key, value in filters.items():
                if value is not None:
                    conditions.append(getattr(receipt_table.c, key) == value)
            stmt = select(receipt_table)
            if conditions:
                stmt = stmt.where(and_(*conditions))
            result = conn.execute(stmt).mappings().all()
        if result:
            return [dict(row) for row in result]
        error_msg = (
            f"Receipt id:{id} not found"
            if id is not None
            else "No receipts found matching criteria"
        )
        raise APIException(error_msg, 404)

    def return_receipt(self, id_receipt: int, id_user: int):
        with engine.connect() as conn:
            if not _verify_user_own_cart(
                conn, id_user, id_receipt, table=receipt_table
            ):
                raise APIException(
                    f"Receipt id:{id_receipt} not owned by user or not exist", 403
                )
            stmt_join = (
                select(
                    cart_item_table.c.id_product,
                    cart_item_table.c.amount.label("amount_receipt"),
                    product_table.c.amount.label("actual_amount"),
                    receipt_table.c.state,
                )
                .select_from(receipt_table)
                .join(cart_table, receipt_table.c.id_cart == cart_table.c.id)
                .join(cart_item_table, cart_table.c.id == cart_item_table.c.id_cart)
                .join(
                    product_table,
                    product_table.c.id == cart_item_table.c.id_product,
                )
                .where(receipt_table.c.id == id_receipt)
            )
            result_join = conn.execute(stmt_join).mappings().all()
            if not result_join:
                raise APIException(
                    f"Receipt id:{id_receipt} not found or has no items", 404
                )
            if result_join[0]["state"] == "returned":
                raise APIException(f"Receipt id{id_receipt}, its already returned", 400)
            products = [
                {
                    "id_product": row["id_product"],
                    "amount_receipt": row["amount_receipt"],
                    "actual_amount": row["actual_amount"],
                }
                for row in result_join
            ]
            for row in products:
                new_amount = row["actual_amount"] + row["amount_receipt"]
                stmt_update_product = (
                    update(product_table)
                    .where(product_table.c.id == row["id_product"])
                    .values(amount=new_amount)
                )
                conn.execute(stmt_update_product)
            stmt_update_receipt = (
                update(receipt_table)
                .where(receipt_table.c.id == id_receipt)
                .values(state="returned")
            )
            conn.execute(stmt_update_receipt)
            conn.commit()

    def __validate_date_str(self, date_str: str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise APIException("Entry date in receipt is not valid", 400)
