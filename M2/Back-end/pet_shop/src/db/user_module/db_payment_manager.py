from sqlalchemy import insert, select, delete, update, and_
from src.db.utils_db.helpers import _filter_locals
from src.utils.helpers import filter_values
from src.db.utils_db.verifies import _verify_user_own_payment
from src.utils.api_exception import APIException


class DbPaymentManager:

    def __init__(self, TablesManager):
        self.payment_table = TablesManager.payment_table
        self.engine = TablesManager.engine

    def insert_data(self, id_user: int, type: str, data: str):
        stmt = (
            insert(self.payment_table)
            .returning(self.payment_table.c.id)
            .values(id_user=id_user, type=type, data=data)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            if result is None:
                raise APIException("Could not create payment", 500)
            conn.commit().scalar()
        return result

    def get_data(
        self,
        id_payment: int | None = None,
        id_user: int | None = None,
        type: str | None = None,
        data: str | None = None,
    ):
        conditions = _filter_locals(self.payment_table, locals())
        stmt = select(self.payment_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with self.engine.connect() as conn:
            if not _verify_user_own_payment(conn, id_payment, id_user):
                raise APIException(f"Payment id:{id_payment} not exist", 404)
            result = conn.execute(stmt)
            rows = result.mappings().all()
            if not result:
                raise APIException(f"Payment id:{id_payment} not exist", 404)
            return [dict(row) for row in result]

    def update_data(
        self, id_payment: int, type: str, data: str, id_user: str | None = None
    ):
        values = filter_values(locals(), ("self", "id_payment", "id_user"))
        stmt = (
            update(self.payment_table)
            .where(self.payment_table.c.id == id_payment)
            .values(**values)
        )
        with self.engine.connect() as conn:
            if not _verify_user_own_payment(conn, id_payment, id_user):
                raise APIException(f"Payment id:{id_payment} not exist", 404)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(
                    f"Payment method id:{str(id_payment)} not exist", 404
                )
            conn.commit()

    def delete_data(self, id_payment: int, id_user: int | None = None):
        stmt = delete(self.payment_table).where(self.payment_table.c.id == id_payment)
        with self.engine.connect() as conn:
            if not _verify_user_own_payment(conn, id_payment, id_user):
                raise APIException(f"Payment id:{id_payment} not exist", 404)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Payment method id:{id_payment} not exist", 404)
            conn.commit()
