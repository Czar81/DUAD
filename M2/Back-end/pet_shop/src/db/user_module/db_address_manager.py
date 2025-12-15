from sqlalchemy import insert, select, delete, update, and_
from src.db.utils_db.helpers import _filter_locals
from src.utils.api_exception import APIException


class DbAddressManager:

    def __init__(self, TablesManager):
        self.address_table = TablesManager.address_table
        self.engine = TablesManager.engine

    def insert_data(self, id_user: int, location: str):
        stmt = (
            insert(self.address_table)
            .returning(self.address_table.c.id)
            .values(id_user=id_user, location=location)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt).scalar()
            if result is None:
                raise APIException("Could not create address", 500)
            conn.commit()
        return result

    def get_data(
        self,
        id_user: int,
        id: int | None = None,
        location: str | None = None,
    ):
        conditions = _filter_locals(self.address_table, locals())
        stmt = select(self.address_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))

        with self.engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            if not result:
                return "Not address found"
            return [dict(row) for row in result]

    def update_data(self, id_user: int, id_address: int, location: str):
        with self.engine.connect() as conn:
            stmt = (
                update(self.address_table)
                .where(
                    and_(
                        self.address_table.c.id == id_address,
                        self.address_table.c.id_user == id_user,
                    )
                )
                .values(location=location)
            )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Address id:{str(id_address)} not exist", 404)
            conn.commit()
        return True

    def delete_data(self, id_user: int, id_address: int):
        with self.engine.connect() as conn:
            stmt = delete(self.address_table).where(
                and_(
                    self.address_table.c.id == id_address,
                    self.address_table.c.id_user == id_user,
                )
            )
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Address id:{str(id_address)} not exist", 404)
            conn.commit()
        return True
