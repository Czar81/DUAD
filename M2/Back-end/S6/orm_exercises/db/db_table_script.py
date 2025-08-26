from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from managers_db.db_user_manager import DbUserManager
from managers_db.db_car_manager import DbCarManager
from managers_db.db_address_manager import DbAddressManager

db_url = "postgresql://postgres:Ian192007@localhost:5432/postgres"
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
    Column("user_id", ForeignKey("users.id")),
)
# Realice un script que valide si las tablas existen, y si no las cree en el momento de su ejecución.
metadata_obj.create_all(engine)

# 1. Crear/Modificar/Eliminar un usuario nuevo.

#user_manager = DbUserManager(user_table, engine, select, insert, update, delete)
# result = user_manager.create_user(name="Mario")
# print(result)
# user_manager.update_user(id=1, name="Samuel")
# user_manager.delete_user(id=1)

# 2. Crear/Modificar/Eliminar un automóvil nuevo.

#car_manager = DbCarManager(cars_table, engine, select, insert, update, delete)
#result = car_manager.create_car(model="Mx5", user_id=1)
#car_manager.update_car(id=1, model="Rx7", user_id="1")
#car_manager.delete_car(id=1)

# 3. Crear/Modificar/Eliminar una dirección nueva.
address_manager = DbAddressManager(address_table, engine, select, insert, update, delete)
result= address_manager.create_address(address="1234 Elmwood Avenue, Apartment 56B, Greenfield Heights, Springfield, Illinois, 62704, United States", user_id=1)
print(result)
address_manager.update_address(id=1, address="789 Maple Street, Floor 3, Suite 305, Downtown Business Center, Toronto, Ontario, M5H 2N2, Canada", user_id=1)
#address_manager.delete_address(id=1)
# 4. Asociar un automóvil a un usuario.
#car_manager.update_user_for_car(id=1, user_id="1")

# 5. Consultar todos los usuarios.
#result = user_manager.get_all_user()
#print(result)

# 6. Consultar todos los automóviles.
#result = car_manager.get_all_cars()
#print(result)

# 7. Consultar todas las direcciones.
result = address_manager.get_all_address()
print(result)
