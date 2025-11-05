from sqlalchemy import insert, select, delete, update, and_
from src.utils.api_exception import APIException
from src.db.utils_db.helpers import _filter_locals, _filter_values


class DbProductManager:

    def __init__(self, TablesManager):
        self.product_table = TablesManager.product_table
        self.engine = TablesManager.engine


    def insert_data(self, sku: str, name: str, price: int, amount: int):
        stmt = (
            insert(self.product_table)
            .returning(self.product_table.c.id)
            .values(sku=sku, name=name, price=price, amount=amount)
        )
        with self.engine.connect() as conn:
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
        conditions = _filter_locals(self.product_table, locals())
        stmt = select(self.product_table)
        if conditions:
            stmt = stmt.where(and_(*conditions))
        with self.engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
        if result:
            return [dict(row) for row in result]
        raise APIException(f"Product id:{id_item} not exist", 404)

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
        stmt = (
            update(self.product_table)
            .where(self.product_table.c.id == id_product)
            .values(**values)
        )
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Product id:{id_product} not exist", 404)
            conn.commit()

    def delete_data(self, id_product: int):
        stmt = delete(self.product_table).where(self.product_table.c.id == id_product)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            if result.rowcount == 0:
                raise APIException(f"Product id:{id_product} not exist", 404)
            conn.commit()
