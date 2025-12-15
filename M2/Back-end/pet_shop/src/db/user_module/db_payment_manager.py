from sqlalchemy import insert, select, delete, update, and_
from src.db.utils_db.helpers import _filter_locals
from src.utils.helpers import filter_values
from src.db.utils_db.verifies import _verify_user_own_payment
from src.utils.api_exception import APIException


class DbPaymentManager:

    def __init__(self, TablesManager):
        self.payment_table = TablesManager.payment_table
        self.engine = TablesManager.engine

    def insert_data(self, id_user: int, type_data: str, data: str):
        stmt = (
            insert(self.payment_table)
            .returning(self.payment_table.c.id)
            .values(id_user=id_user, type_data=type_data, data=data)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            if result is None:
                raise APIException("Could not create payment", 500)
            conn.commit()
        return result

    def get_data(
        self,
        id_user: int,
        id: int | None = None,
        type_data: str | None = None,
    ):
        conditions = _filter_locals(self.payment_table, locals())
        stmt = select(self.payment_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with self.engine.connect() as conn:     
            result = conn.execute(stmt).mappings().all()
            if not result:
                return "Not payments found"
            return [dict(row) for row in result]

    def update_data(
        self, id: int, type_data: str, data: str, id_user: str
    ):
        values = filter_values(locals(), ("self", "id", "id_user"))
        stmt = (
            update(self.payment_table)
            .where(and_(self.payment_table.c.id == id, self.payment_table.c.id_user == id_user))
            .values(**values)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(
                    f"Payment method id:{str(id)} not exist", 404
                )
            conn.commit()
        return True

    def delete_data(self, id: int, id_user: int):
        stmt = delete(self.payment_table).where(and_(self.payment_table.c.id == id, self.payment_table.c.id_user == id_user))
        with self.engine.connect() as conn:
            if not _verify_user_own_payment(conn, id, id_user):
                raise APIException(f"Payment id:{id} not exist", 404)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Payment method id:{id} not exist", 404)
            conn.commit()
        return True
