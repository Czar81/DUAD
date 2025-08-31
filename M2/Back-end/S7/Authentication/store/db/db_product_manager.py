from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DATE
from sqlalchemy import insert, select

metadata_obj = MetaData()

product_table = Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("price", Integer(30)),
    Column("entry_date", DATE),
    Column("amount", Integer(10))
)

class DbProductManager:
    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2://postgres:fasd89fa7gs98@localhost:5432/postgres')
        metadata_obj.create_all(self.engine)
    
    def insert_product(self, name, price, entry_date, amount):
        stmt = insert(product_table).returning(product_table.c.id).values(name=name, price=price, entry_date=entry_date, amount=amount)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_products(self):
        stmt = select(product_table)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()

    def get_product_by_id(self,id):
        stmt = select(product_table).where(id=id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if(len(users)==0):
                return None
            else:
                return users[0]

    def update_product(self, id, name, price, entry_date, amount):
        stmt = update(product_table).where(id=id).values(name=name, price=price, entry_date=entry_date, amount=amount)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows.created = result.rowcount()
            if (len(rows.created)==0):
                    return None
            else:
                return rows.created

    def delete_product(self, id):
        stmt = delete(product_table).where(id=id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount()
            if (len(rows_deleted)==0):
                    return None
            else:
                return rows_deleted
