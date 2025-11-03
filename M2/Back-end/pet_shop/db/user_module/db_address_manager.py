from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import _filter_locals, _verify_user_own_address
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
            if not _verify_user_own_address(conn, id_address, id_user):
                raise APIException(f"Address id:{id_address} not exist", 404)
            result = conn.execute(stmt).mappings().all()
            if result:
                return [dict(row) for row in result]
            raise APIException(f"Address id:{id_item} not exist",404)

    def update_data(self, id_address: int, location: str, id_user: str | None = None):
        with engine.connect() as conn:
            if not _verify_user_own_address(conn, id_address, id_user):
                raise APIException(f"Address id:{id_address} not exist", 404)
            stmt = update(address_table).where(address_table.c.id == id_address).values(location=location)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Address id:{str(id_address)} not exist",404)
            conn.commit()

    def delete_data(self, id_address: int, id_user: int | None = None):
        with engine.connect() as conn:
            if not _verify_user_own_address(conn, id_address, id_user):
                raise APIException(f"Address id:{id_address} not exist", 404)
            stmt = delete(address_table).where(address_table.c.id == id_address)
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Address id:{str(id_address)} not exist",404)
            conn.commit()
