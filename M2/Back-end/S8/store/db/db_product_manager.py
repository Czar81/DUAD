from sqlalchemy import insert, select, delete, update
from db.tables_manager import TablesManager
from utils.api_exception import APIException

product_table = TablesManager.product_table
engine = TablesManager.engine


class DbProductManager:

    def insert_product(self, name: str, price: int, amount: int):
        stmt = (
            insert(product_table)
            .returning(product_table.c.id)
            .values(name=name, price=price, amount=amount)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_products(self):
        stmt = select(product_table)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            products = [dict(row) for row in result.mappings().all()]
            return products

    def get_product_by_id(self, id: int):
        stmt = select(product_table).where(product_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            product = result.all()
            if len(product) == 0:
                raise APIException(f"Product id:{str(id)} does not exist", 404)
            else:
                return dict(product)

    def update_product(self, id: int, name: str, price: int, amount: int):
        stmt = (
            update(product_table)
            .where(product_table.c.id == id)
            .values(name=name, price=price, amount=amount)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(f"Product id:{str(id)} not exist", 404)
            else:
                conn.commit()

    def delete_product(self, id: int):
        stmt = delete(product_table).where(product_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(f"Product id:{str(id)} not exist", 403)
            else:
                conn.commit()
