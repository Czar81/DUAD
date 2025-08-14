from flask import Flask
from api.car_rental_api import CarRentalView
from scripts.database.user_repository import UserRepository
from scripts.database.car_repository import CarRepository
from scripts.database.rent_repository import RentRepository
from scripts.database.pg_manager import PgManager

app = Flask(__name__)
db_manager = PgManager(
    db_name="postgres", user="postgres", password="Ian192007", host="localhost"
)
user_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rent_repo = RentRepository(db_manager)

app.add_url_rule("/user", view_func=CarRentalView.as_view("user",user_repo))
app.add_url_rule("/user/<int:id>", view_func=CarRentalView.as_view("users",user_repo))
app.add_url_rule("/car", view_func=CarRentalView.as_view("cars", car_repo))
app.add_url_rule("/car/<int:id>", view_func=CarRentalView.as_view("car", car_repo))
app.add_url_rule("/rent", view_func=CarRentalView.as_view("rents", rent_repo))
app.add_url_rule("/rent/<int:id>", view_func=CarRentalView.as_view("rent", rent_repo))

app.run(debug=True, host="localhost", port=5000)
