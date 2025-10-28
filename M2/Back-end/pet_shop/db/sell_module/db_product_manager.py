from sqlalchemy import insert, select, delete, update, and_
from utils.api_exception import APIException
from db.utils_db.tables_manager import TablesManager
from db.utils_db.helpers import _filter_locals, _filter_values

product_table = TablesManager.product_table
engine = TablesManager.engine


class DbProductManager:

    def insert_data(self, sku: str, name: str, price: int, amount: int):
        stmt = (
            insert(product_table)
            .returning(product_table.c.id)
            .values(sku=sku, name=name, price=price, amount=amount)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.scalar()

    def get_data(
        self,
        id_product: int | None = None,
        sku: str | None = None,
        name: str | None = None,
        price: int | None = None,
        amount: int | None = None,
    ):
        conditions = _filter_locals(product_table,locals())
        stmt = select(product_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with engine.connect() as conn:
            result = conn.execute(stmt)
        return [dict(row) for row in result.mappings().all()]

    def update_data(
        self,
        id_product: int,
        sku: str | None = None,
        name: str | None = None,
        price: int | None = None,
        amount: int | None = None,
    ):
        values = _filter_values(locals(), ("self", "id_product"))
        if values is None:
            raise APIException("No provide any value", 400)
        stmt = update(product_table).where(product_table.c.id == id_product).values(**values)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_updated = result.rowcount
            if rows_updated == 0:
                raise APIException(f"Product id:{id_product} not exist", 404)
            conn.commit()

    def delete_data(self, id_product: int):
        stmt = delete(product_table).where(product_table.c.id == id_product)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(f"Product id:{id_product)} not exist", 404)
            conn.commit()
