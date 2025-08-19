from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

db_url = 'postgresql://postgres:Ian192007@localhost:5432/postgres'
engine = create_engine(db_url, echo=True)

metadata_obj = MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer(), primary_key=True),
    Column("name", String(30), nullable=False),
)
address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer(), primary_key=True),
    Column("address", String(), nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=False),
)

cars_table = Table(
    "cars",
    metadata_obj,
    Column("id", Integer(), primary_key=True),
    Column("model", String(30), nullable=False),
    Column("user_id", ForeignKey("users.id"))
)

metadata_obj.create_all(engine)