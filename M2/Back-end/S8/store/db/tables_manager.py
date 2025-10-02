from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DATE, func
from dotenv import load_dotenv
from os import environ
load_dotenv()

class TablesManager:
    engine = create_engine(os.environ.get("URL_POSTGRES"))
    metadata_obj = MetaData()
    product_table = Table(
        "products",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("price", Integer()),
        Column("entry_date", DATE, server_default=func.now()),
        Column("amount", Integer()),
    )
    user_table = Table(
        "users",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("username", String(30)),
        Column("password", String),
        Column("role", String(10), server_default="user"),
    )
    receipt_table = Table(
        "receipt",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("id_user", Integer, ForeignKey("users.id")),
    )
    receipt_details_table = Table(
        "receipt_details",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("id_receipt", Integer, ForeignKey("receipt.id")),
        Column("id_product", Integer, ForeignKey("products.id")),
        Column("amount", Integer),
    )

    @classmethod
    def create_tables(cls):
        cls.metadata_obj.create_all(cls.engine)
