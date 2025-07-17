from database.pg_manager import PgManager
from database.user_repository import UserRepository
from database.car_repository import CarRepository
from database.rent_repository import RentRepository

if __name__ == "__main__":
    db_manager = PgManager(
        db_name="postgres", user="postgres", password="postgres", host="localhost"
    )
    # a. Un script que agregue un usuario nuevo
    users_rep = UserRepository(db_manager)
    users_rep.create_user(
        name="Darrell Weber",
        email="siuzlow@maleseget.so",
        username="Darr123",
        password="Weber1984",
        birthday="1984-12-05",
        state="Renting",
    )
    # b. Un script que agregue un automovil nuevo
    cars_repo = CarRepository(db_manager)
    cars_repo.create_car(make="BMW", model="M3 GTR", year=2005, state="Rented")
    # c. Un script que cambie el estado de un usuario
    users_rep.chage_user_state(user_id=51, new_state="")
    # d. Un script que cambie el estado de un automovil
    cars_repo.chage_car_state(car_id=26, new_state="Available")
    # e. Un script que genere un alquiler nuevo con los datos de un usuario y un automovil
    rents_repo = RentRepository(db_manager)
    rents_repo.create_rent(fk_car_id=26, fk_user_id=51, state="Rented")
    # f. Un script que confirme la devolución del auto al completar el alquiler, colocando el auto como disponible y completando el estado del alquiler
    rents_repo.car_returned(rent_id=26)
    # g. Un script que deshabilite un automovil del alquiler
    cars_repo.disable_car(car_id=26)
    # h. Un script que obtenga todos los automoviles alquilados, y otro que obtenga todos los disponibles.
    print(cars_repo.get_rented())
    print(cars_repo.get_available())
