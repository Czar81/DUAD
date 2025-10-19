from sqlalchemy import insert, select, delete, update
from db.tables_manager import TablesManager
from utils.api_exception import APIException
from utils.helpers import filter_locals, verify_user_own_cart
from datetime import datetime

receipt_table = TablesManager.receipt_table
engine = TablesManager.engine


class DbReceiptManager:

    def create_receipt(self, id_cart: int, id_address: int, id_payment: int):
        stmt = (
            insert(receipt_table)
            .returning(receipt_table.c.id)
            .values(id_cart=id_cart, id_address=id_address, id_payment=id_payment)
        )

        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.scalar()

    def get_receipt(
        self,
        id: int | None = None,
        id_user: int | None = None,
        id_cart: int | None = None,
        id_address: int | None = None,
        id_product: int | None = None,
        entry_date: str | None = None,
        state: str | None = None,
    ):
        filters = filter_locals(
            locals(),
            (
                "self",
                "id_user",
            ),
        )
        conditions = []
        with engine.connect() as conn:
            if id_user is not None and not verify_user_own_cart(
                conn, id, id_user, receipt_table
            ):
                raise APIException(
                    f"Receipt id:{id} not owned by user id:{id_user}", 403
                )
            if entry_date is not None:
                __validate_date_str(entry_date, "Entry date in receipt is not valid")
            for key, value in filters.items():
                if value is not None:
                    conditions.append(getattr(receipt_table.c, key) == value)
            stmt = select(receipt_table)
            if conditions:
                stmt = stmt.where(and_(*conditions))
            result = conn.execute(stmt).mappings().all()
        return result

    def update_receipt(
        self,
        id: int,
        id_user: int | None = None,
        id_cart: int | None = None,
        id_address: int | None = None,
        id_product: int | None = None,
        entry_date: str | None = None,
        state: str | None = None,
    ):
        if entry_date:
            __validate_date_str(entry_date, "Entry date in receipt is not valid")
        values = filter_locals(locals(), ("self", "id", "id_user"))

        stmt = update(receipt_table).where(receipt_table.c.id == id)
        if values:
            stmt = stmt.values(**values)
        # hacer join en cart para obtener user
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
        if rows_updated == 0:
            raise APIException(
                (
                    f"Recipt id:{str(id)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Recipt id:{str(id)} not exist"
                ),
                404,
            )
        conn.commit()

    def delete_receipt(self, id: int):
        stmt = delete(receipt_table).where(receipt_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
        if rows_deleted == 0:
            raise APIException(
                (f"Recipt id:{str(id)} not exist"),
                404,
            )
        conn.commit()

    def __validate_date_str(date_str: str, message: str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise APIException(message, 401)
