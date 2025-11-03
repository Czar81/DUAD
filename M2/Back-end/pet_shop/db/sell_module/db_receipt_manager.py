from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import _filter_locals, _filter_values, _verify_user_own_cart
from utils.api_exception import APIException
from datetime import datetime

receipt_table = TablesManager.receipt_table
engine = TablesManager.engine


class DbReceiptManager:

    def insert_data(self, id_cart: int, id_address: int, id_payment: int, state: str | None = None):
        stmt = (
            insert(receipt_table)
            .returning(receipt_table.c.id)
            .values(id_cart=id_cart, id_address=id_address, id_payment=id_payment, state=state)
        )

        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.scalar()

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
        filters = _filter_locals(receipt_table,
            locals(),
            (
                "self",
                "id_user",
            ),
        )
        conditions = []
        with engine.connect() as conn:
            if id_user is not None and not _verify_user_own_cart(
                conn, id, id_user, receipt_table
            ):
                raise APIException(
                    f"Receipt id:{id_item} not exist", 403
                )
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
        raise APIException(f"Receipt id:{id_item} not exist",404)

    def update_data(
        self,
        id_receipt: int,
        id_user: int | None = None,
        id_cart: int | None = None,
        entry_date: str | None = None,
        state: str | None = None,
    ):
        if entry_date:
            self.__validate_date_str(entry_date)
        values = _filter_values(locals(), ("self", "id_receipt", "id_user", "id_cart"))

        stmt = update(receipt_table).where(receipt_table.c.id == id_receipt)
        if values:
            stmt = stmt.values(**values)
        with engine.connect() as conn:
            if id_user is not None and not _verify_user_own_cart(
                conn, id_user, id_cart=id_cart
            ):
                raise APIException(f"Recipt id:{id_receipt} not exist", 403)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException((f"Recipt id:{id_receipt} not exist"),404)
            conn.commit()

    def delete_data(self, id_receipt: int, id_user:int|None= None):
        with engine.connect() as conn:
            if id_user is not None and not _verify_user_own_cart(
                conn=conn, id_user=id_user, id_table=id_receipt, table=receipt_table
            ):
                raise APIException(f"Recipt id:{id_receipt} not exist", 403)
            stmt = delete(receipt_table).where(receipt_table.c.id == id_receipt)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException((f"Recipt id:{id_receipt} not exist"),404)
            conn.commit()

    def __validate_date_str(date_str: str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise APIException("Entry date in receipt is not valid", 401)
