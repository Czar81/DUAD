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

    def get_addresss(self):
        stmt = select(address_table)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            return [dict(row) for row in result.mappings().all()]

    def get_address_by_user_id(self, id_user: int):
        stmt = select(address_table).where(address_table.c.id_user == id_user)
        with engine.connect() as conn:
            result = conn.execute(stmt).mappings().first()
            if result is not None:
                return [dict(row) for row in result.mappings().all()]
            else:
                raise APIException(f"User id:{str(id)} does not have any address", 404)

    def update_address(self, id: int, id_user: str, location: str):
        stmt = (
            update(address_table)
            .where(address_table.c.id == id)
            .values(id_user=id_user, location=location)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(f"Address id:{str(id)} not exist", 404)
            else:
                conn.commit()
    def update_address(self, id: int, id_user: str, location: str):
        stmt = (
            update(address_table)
            .where(address_table.c.id == id, product_table.c.id_user==id_user)
            .values(location=location)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(f"Address id:{str(id)} not exist", 404)
            else:
                conn.commit()

    def delete_address(self, id: int):
        stmt = delete(address_table).where(address_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(f"Address id:{str(id)} not exist", 404)
            else:
                conn.commit()

    def delete_own_address(self, id: int, id_user: int):
        stmt = delete(address_table).where(
            address_table.c.id == id, address_table.c.id_user == id_user
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(f"Address id:{str(id)} not exist", 404)
            else:
                conn.commit()
