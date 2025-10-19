from sqlalchemy import insert, select, delete, update
from .tables_manager import TablesManager
from utils.api_exception import APIException
from utils.helpers import filter_locals

address_table = TablesManager.address_table
engine = TablesManager.engine


class DbAddressManager:

    def insert_address(self, id_user: str, location: str):
        stmt = (
            insert(address_table)
            .returning(address_table.c.id)
            .values(id_user=id_user, location=location)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_addresss(
        self,
        id: int | None = None,
        id_user: int | None = None,
        location: str | None = None,
    ):
        params = filter_locals(locals())
        conditions = []
        for key, value in filters.items():
            if value is not None:
                conditions.append(getattr(address_table.c, key) == value)
        stmt = select(address_table)
        if conditions:
            stmt = stmt.where(*conditions)

        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result is not None:
                return [dict(row) for row in result.mappings().all()]
            raise APIException(
                (
                    f"Address id:{str(id)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Address id:{str(id)} not exist"
                ),
                404,
            )

    def update_address(self, id: int, location: str, id_user: str | None = None):
        conditions = [address_table.c.id == id]
        if id_user is not None:
            conditions.append(address_table.c.id_user == id_user)
        stmt = update(address_table).where(*conditions).values(location=location)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated != 0:
                conn.commit()
            raise APIException(
                (
                    f"Address id:{str(id)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Address id:{str(id)} not exist"
                ),                    
                404,
            )

    def delete_address(self, id: int, id_user: int | None = None):
        conditions = [address_table.c.id == id]
        if id_user is not None:
            conditions.append(address_table.c.id_user == id_user)
        stmt = delete(address_table).where(address_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted != 0:
                conn.commit()
            raise APIException(
                (
                    f"Address id:{str(id)} not exist or not owned by user id:{id_user}"
                    if id_user
                    else f"Address id:{str(id)} not exist"
                ),                    
                404,
            )
