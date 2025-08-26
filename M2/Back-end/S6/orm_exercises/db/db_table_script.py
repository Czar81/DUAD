from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from managers_db.db_user_manager import DbUserManager
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete

db_url = "postgresql://postgres:postgres@localhost:5432/postgres"
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
    Column("long_address", String(), nullable=False),
    Column("user_id", ForeignKey("users.id"), nullable=False),
)

cars_table = Table(
    "cars",
    metadata_obj,
    Column("id", Integer(), primary_key=True),
    Column("model", String(30), nullable=False),
    Column("user_id", ForeignKey("users.id")),
)

metadata_obj.create_all(engine)

# 1. Crear/Modificar/Eliminar un usuario nuevo.
user_manager = DbUserManager(user_table, engine, select, insert, update, delete)
result = user_manager.create_user(name="Mario")
print(result)
result = user_manager.update_user(id=1, name="Samuel")
user_manager.delete_user(id=2)
# 2. Crear/Modificar/Eliminar un automóvil nuevo.
# 3. Crear/Modificar/Eliminar una dirección nueva.
# 4. Asociar un automóvil a un usuario.
# 5. Consultar todos los usuarios.
result=user_manager.get_all_user()
print(result)
# 6. Consultar todos los automóviles.
# 7. Consultar todas las direcciones.
