from sqlalchemy import insert, select, delete, update
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import filter_locals
from utils.api_exception import APIException

payment_table = TablesManager.payment_table
engine = TablesManager.engine


class DbPaymentManager:

    def insert(self, id_user: str, type: str, data: str):
        stmt = (
            insert(payment_table)
            .returning(payment_table.c.id)
            .values(id_user=id_user, type=type, data=data)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get(
        self,
        id: int | None = None,
        id_user: int | None = None,
        type: str | None = None,
        data: str | None = None,
    ):
        params = filter_locals(locals())

        conditions = []
        for key, value in params.items():
            if value is not None:
                conditions.append(getattr(payment_table.c, key) == value)
        stmt = select(payment_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        stmt = select(payment_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result is not None:
                return [dict(row) for row in result.mappings().all()]
            raise APIException(
                (
                    f"Payment method id:{str(id)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Payment method id:{str(id)} not exist"
                ),
                404,
            )

    def update(self, id: int, type: str, data: str, id_user: str | None = None):
        conditions = [payment_table.c.id == id]
        if id_user is not None:
            conditions.append(payment_table.c.id_user == id_user)
        stmt = (
            update(payment_table)
            .where(*conditions)
            .values(type=type, data=data)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated != 0:
                conn.commit()
            raise APIException(
                (
                    f"Payment method id:{str(id)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Payment method id:{str(id)} not exist"
                ),                    
                404,
            )

    def delete(self, id: int, id_user: int | None = None):
        conditions = [payment_table.c.id == id]
        if id_user is not None:
            conditions.append(payment_table.c.id_user == id_user)
        stmt = delete(payment_table).where(payment_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted != 0:
                conn.commit()
            raise APIException(
                (
                    f"Payment method id:{str(id)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Payment method id:{str(id)} not exist"
                ),                    
                404,
            )
