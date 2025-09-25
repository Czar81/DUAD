from sqlalchemy import insert, select, update
from db.db_product_manager import product_table
from db.tables_manager import TablesManager
from api_exception import APIException

receipt_table = TablesManager.receipt_table
receipt_details_table = TablesManager.receipt_details_table
engine = TablesManager.engine


class DbReceiptManager:

    def create_receipt(self, id_user: int, id_product: int, amount: int):
        with engine.connect() as conn:
            valid, new_amount = self.__verify_amount(id_product, amount)
            if valid == False:
                raise APIException(
                    f"Can not buy {amount} units, only {new_amount} available"
                )

            stmt_receipt = (
                insert(receipt_table)
                .returning(receipt_table.c.id)
                .values(id_user=id_user)
            )
            receipt_id = conn.execute(stmt_receipt).scalar()

            stmt_detail = (
                insert(receipt_details_table)
                .returning(receipt_details_table.c.id)
                .values(id_receipt=receipt_id, id_product=id_product, amount=amount)
            )
            receipt_datails_id = conn.execute(stmt_detail).scalar()

            stmt_product_reduce = (
                update(product_table)
                .where(product_table.c.id == id_product)
                .values(amount=new_amount)
            )
            conn.execute(stmt_product_reduce)

            conn.commit()
            return receipt_id, receipt_datails_id

    def get_receipt_by_user_id(self, id_user: int):
        stmt = select(receipt_table).where(receipt_table.c.id_user == id_user)
        with engine.connect() as conn:
            results = conn.execute(stmt)
            receipts = [dict(row) for row in results.mappings().all()]
            return receipts

    def __verify_amount(self, id_product, amount):
        with engine.connect() as conn:
            stmt_product_get_amount = select(product_table.c.amount).where(
                product_table.c.id == id_product
            )
            amount_product = conn.execute(stmt_product_get_amount).scalar
            new_amount = amount_product - amount
        if new_amount < 0:
            return False, amount_product
        else:
            return new_amount
