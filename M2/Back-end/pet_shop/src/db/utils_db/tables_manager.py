from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from dotenv import load_dotenv
from datetime import date
from os import environ

load_dotenv()


class TablesManager:
    def __init__(self, url=environ.get("URL_POSTGRES")):
        self.engine = create_engine(url)
    metadata_obj = MetaData()
    product_table = Table(
        "product",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("sku", String(20), nullable=False),
        Column("name", String(30), nullable=False),
        Column("price", Integer, nullable=False),
        Column("amount", Integer, nullable=False),
    )
    user_table = Table(
        "user",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30), nullable=False),
        Column("password", String, nullable=False),
        Column("role", String(10), server_default="user"),
    )
    cart_table = Table(
        "cart",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("id_user", Integer, ForeignKey("user.id")),
        Column("state", String(10), server_default="active"),
    )
    address_table = Table(
        "address",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("id_user", Integer, ForeignKey("user.id")),
        Column("location", String(30), nullable=False),
    )
    payment_table = Table(
        "payment",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("id_user", Integer, ForeignKey("user.id")),
        Column("type", String(10), nullable=False),
        Column("data", String(30)),
    )
    cart_item_table = Table(
        "cart_item",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("id_cart", Integer, ForeignKey("cart.id")),
        Column("id_product", Integer, ForeignKey("product.id")),
        Column("amount", Integer, nullable=False),
    )
    receipt_table = Table(
        "receipt",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("id_cart", Integer, ForeignKey("cart.id")),
        Column("id_address", Integer, ForeignKey("address.id")),
        Column("id_payment", Integer, ForeignKey("payment.id")),
        Column("entry_date", String(10), server_default=str(date.today())),
        Column("state", String(10), server_default="bought"),
    )

    def create_tables(self):
        self.metadata_obj.create_all(self.engine)
