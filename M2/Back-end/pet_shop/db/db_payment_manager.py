from sqlalchemy import insert, select, delete, update
from .tables_manager import TablesManager
from utils.api_exception import APIException

payment_table = TablesManager.payment_table
engine = TablesManager.engine


class DbPaymentManager:

    def insert_payment(self, id_user: str, type: str, data: str):
        stmt = (
            insert(payment_table)
            .returning(payment_table.c.id)
            .values(id_user=id_user, type=type, data=data)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_payments(self):
        stmt = select(payment_table)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            payments = [dict(row) for row in result.mappings().all()]
            return payments

    def get_payment_by_user_id(self, id_user: int):
        stmt = select(payment_table).where(payment_table.c.id_user == id_user)
        with engine.connect() as conn:
            result = conn.execute(stmt).mappings().first()
            if result is not None:
                return dict(result)
            else:
                raise APIException(
                    f"User id:{str(id)} does not have any payments methods", 404
                )

    def update_payment(self, id: int, id_user: int, type: str, data: str):
        stmt = (
            update(payment_table)
            .where(payment_table.c.id == id)
            .values(id_user=id_user, type=type, data=data)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(f"Payment id:{str(id)} not exist", 404)
            else:
                conn.commit()

    def update_own_payment(self, id: int, id_user: int, type: str, data: str):
        stmt = (
            update(payment_table)
            .where(payment_table.c.id == id, payment_table.c.id_user == id_user)
            .values(type=type, data=data)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(f"Payment id:{str(id)} not exist", 404)
            else:
                conn.commit()

    def delete_payment(self, id: int):
        stmt = delete(payment_table).where(payment_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(f"Payment id:{str(id)} not exist", 404)
            else:
                conn.commit()

    def delete_own_payment(self, id: int, id_user: int):
        stmt = delete(payment_table).where(
            payment_table.c.id == id, payment_table.c.id_user == id_user
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(f"Payment id:{str(id)} not exist", 404)
            else:
                conn.commit()
