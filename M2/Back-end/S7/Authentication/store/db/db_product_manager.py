from sqlalchemy import insert, select, delete, update
from db.tables_manager import TablesManager

product_table = TablesManager.product_table
engine = TablesManager.engine


class DbProductManager:

    def insert_product(self, name: str, price: int, amount: int):  # Create try except
        stmt = (
            insert(product_table)
            .returning(product_table.c.id)
            .values(name=name, price=price, amount=amount)
        )
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_products(self):  # Create try except
        stmt = select(product_table)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            products = [dict(row) for row in result.mappings().all()]
            return products

    def get_product_by_id(self, id: int):
        # Do a select for id
        stmt = select(product_table).where(id=id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            products = result.all()
            if len(products) == 0:
                return None  # Create try except
            else:
                return products

    def update_product(self, id: int, name: str, price: int, amount: int):
        # Do a select for id
        stmt = (
            update(product_table)
            .where(product_table.c.id == id)
            .values(name=name, price=price, amount=amount)
        )

        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                return None  # Create try except and raise
            else:
                conn.commit()

    def delete_product(self, id: int):
        # Do a select for id
        stmt = delete(product_table).where(product_table.c.id == id)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                return None  # Create try except
            else:
                conn.commit()
