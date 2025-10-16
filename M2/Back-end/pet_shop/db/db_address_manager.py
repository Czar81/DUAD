from sqlalchemy import insert, select, delete, update
from .tables_manager import TablesManager
from utils.api_exception import APIException

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

    def get_addresss(self, id: int | None = None, id_user: int | None = None):
        conditions = []
        if id is not None:
            conditions.append(address_table.c.id == id)
        if id_user is not None:
            conditions.append(address_table.c.id_user == id_user)

        stmt = select(address_table)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            if result is not None:
                return [dict(row) for row in result.mappings().all()]
            else:
                raise APIException(f"User id:{str(id)} does not have any address", 404)

    def update_address(self, id: int, id_user: str, location: str):
        conditions = [address_table.c.id == id]
         if id_user is not None:
            conditions.append(address_table.c.id_user == id_user)
        stmt = (
            update(address_table)
            .where(*conditions)
            .values(location=location)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(
                    (
                        f"Address id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Address id:{str(id)} not exist"
                    ),
                    404,
                )
            conn.commit()

    def delete_address(self, id: int, id_user: int | None = None):
        conditions = [address_table.c.id == id]
        if id_user is not None:
            conditions.append(address_table.c.id_user == id_user)
        stmt = delete(address_table).where(address_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
           if rows_deleted == 0:
                raise APIException(
                    (
                        f"Address id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Address id:{str(id)} not exist"
                    ),
                    404,
                )
            conn.commit()