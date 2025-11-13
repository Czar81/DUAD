from sqlalchemy import insert, select, delete, update, and_
from src.db.utils_db.helpers import _filter_locals
from src.db.utils_db.verifies import _verify_user_own_address
from src.utils.api_exception import APIException



class DbAddressManager:

    def __init__(self, TablesManager):
        self.address_table = TablesManager.address_table
        self.engine = TablesManager.engine

    def insert_data(self, id_user: str, location: str):
        stmt = (
            insert(self.address_table)
            .returning(self.address_table.c.id)
            .values(id_user=id_user, location=location)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_data(
        self,
        id_address: int | None = None,
        id_user: int | None = None,
        location: str | None = None,
    ):
        conditions = _filter_locals(self.address_table, locals())
        stmt = select(self.address_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))

        with self.engine.connect() as conn:
            if not _verify_user_own_address(conn, id_address, id_user):
                raise APIException(f"Address id:{id_address} not exist", 404)
            result = conn.execute(stmt).mappings().all()
            if result:
                return [dict(row) for row in result]
            raise APIException(f"Address id:{id_item} not exist", 404)

    def update_data(self, id_address: int, location: str, id_user: str | None = None):
        with self.engine.connect() as conn:
            if not _verify_user_own_address(conn, id_address, id_user):
                raise APIException(f"Address id:{id_address} not exist", 404)
            stmt = (
                update(self.address_table)
                .where(self.address_table.c.id == id_address)
                .values(location=location)
            )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Address id:{str(id_address)} not exist", 404)
            conn.commit()

    def delete_data(self, id_address: int, id_user: int | None = None):
        with self.engine.connect() as conn:
            if not _verify_user_own_address(conn, id_address, id_user):
                raise APIException(f"Address id:{id_address} not exist", 404)
            stmt = delete(self.address_table).where(self.address_table.c.id == id_address)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Address id:{str(id_address)} not exist", 404)
            conn.commit()
