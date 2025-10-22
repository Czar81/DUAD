from sqlalchemy import insert, select, delete, update, and_
from db.utils_db.tables_manager import TablesManager
from utils.api_exception import APIException
from utils.helpers import filter_locals

product_table = TablesManager.product_table
engine = TablesManager.engine


class DbProductManager:

    def insert_product(self, sku: str, name: str, price: int, amount: int):
        stmt = (
            insert(product_table)
            .returning(product_table.c.id)
            .values(sku=sku, name=name, price=price, amount=amount)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.scalar()

    def get_products(
        self,
        id: int | None = None,
        sku: str | None = None,
        name: str | None = None,
        price: int | None = None,
        amount: int | None = None,
    ):
        params = filter_locals(locals())

        conditions = []
        for key, value in params.items():
            if value is not None:
                conditions.append(getattr(product_table.c, key) == value)
        stmt = select(product_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt)
        return [dict(row) for row in result.mappings().all()]

    def update_product(
        self,
        id: int,
        sku: str | None = None,
        name: str | None = None,
        price: int | None = None,
        amount: int | None = None,
    ):
        values = filter_locals(locals(), ("self", "id"))
        stmt = update(product_table).where(product_table.c.id == id)
        if values:
            stmt = stmt.values(**value)
        else:
            raise APIException("No provide any value", 400)

        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
        if rows_updated == 0:
            raise APIException(f"Product id:{str(id)} not exist", 404)
        conn.commit()

    def delete_product(self, id: int, id: int | None = None):
        conditions = [product_table.c.id == id]
        if id_user is not None:
            conditions.append(product_table.c.id_user == id_user)
        stmt = delete(product_table).where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
        if rows_deleted != 0:
            conn.commit()
        raise APIException(f"Product id:{str(id)} not exist", 404)
