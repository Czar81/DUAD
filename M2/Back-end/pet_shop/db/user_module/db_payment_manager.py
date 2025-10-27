from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import _filter_locals, _filter_values
from utils.api_exception import APIException

payment_table = TablesManager.payment_table
engine = TablesManager.engine


class DbPaymentManager:

    def insert_data(self, id_user: str, type: str, data: str):
        stmt = (
            insert(payment_table)
            .returning(payment_table.c.id)
            .values(id_user=id_user, type=type, data=data)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_data(
        self,
        id: int | None = None,
        id_user: int | None = None,
        type: str | None = None,
        data: str | None = None,
    ):
        conditions = _filter_locals(payment_table ,locals())
        stmt = select(payment_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows = result.mappings().all()
            if rows:
                return [dict(row) for row in rows]
            raise APIException(
                (
                    f"Payment method id:{str(id)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Payment method id:{str(id)} not exist"
                ),
                404,
            )

    def update_data(self, id: int, type: str, data: str, id_user: str | None = None):
        values = _filter_values(locals(), ("self","id", "id_user"))
        conditions = [payment_table.c.id == id]
        if id_user is not None:
            conditions.append(payment_table.c.id_user == id_user)
        stmt = (
            update(payment_table)
            .where(*conditions)
            .values(**values)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated == 0:
                raise APIException(
                    (
                        f"Payment method id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Payment method id:{str(id)} not exist"
                    ),                    
                    404,
                )
            conn.commit()    

    def delete_data(self, id: int, id_user: int | None = None):
        conditions = [payment_table.c.id == id]
        if id_user is not None:
            conditions.append(payment_table.c.id_user == id_user)
        stmt = delete(payment_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(
                    (
                        f"Payment method id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Payment method id:{str(id)} not exist"
                    ),                    
                    404,
                )
            conn.commit()
