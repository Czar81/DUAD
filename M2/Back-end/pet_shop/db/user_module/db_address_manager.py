from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import _filter_locals
from utils.api_exception import APIException

address_table = TablesManager.address_table
engine = TablesManager.engine


class DbAddressManager:

    def insert_data(self, id_user: str, location: str):
        stmt = (
            insert(address_table)
            .returning(address_table.c.id)
            .values(id_user=id_user, location=location)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_data(
        self,
        id_address: int | None = None,
        id_user: int | None = None,
        location: str | None = None,
    ):
        conditions = _filter_locals(address_table,locals())
        stmt = select(address_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))

        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result is not None:
                return [dict(row) for row in result.mappings().all()]
            raise APIException(
                (
                    f"Address id:{str(id_address)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Address id:{str(id_address)} not exist"
                ),
                404,
            )

    def update_data(self, id_address: int, location: str, id_user: str | None = None):
        conditions = [address_table.c.id == id_address]
        if id_user is not None:
            conditions.append(address_table.c.id_user == id_user)
        stmt = update(address_table).where(*conditions).values(location=location)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated == 0:
                raise APIException(
                    (
                        f"Address id:{str(id_address)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Address id:{str(id_address)} not exist"
                    ),                    
                    404,
                )
            conn.commit()

    def delete_data(self, id_address: int, id_user: int | None = None):
        conditions = [address_table.c.id == id_address]
        if id_user is not None:
            conditions.append(address_table.c.id_user == id_user)
        stmt = delete(address_table).where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(
                    (
                        f"Address id:{str(id_address)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Address id:{str(id_address)} not exist"
                    ),                    
                    404,
                )
            conn.commit()
