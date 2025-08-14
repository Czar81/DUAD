from flask import Flask
from api.user_api import UserView
from api.car_api import CarView
from api.rent_api import RentView
from scripts.database.user_repository import UserRepository
from scripts.database.car_repository import CarRepository
from scripts.database.rent_repository import RentRepository
from scripts.database.pg_manager import PgManager

app = Flask(__name__)
db_manager = PgManager(
    db_name="postgres", user="postgres", password="postgress", host="localhost"
)
user_repo = UserRepository(db_manager)
car_repo = CarRepository(db_manager)
rent_repo = RentRepository(db_manager)

app.add_url_rule("/user/<int:id>", view_func=UserView.as_view("user",user_repo))
app.add_url_rule("/car/<int:id>", view_func=CarView.as_view("car", car_repo))
app.add_url_rule("/rent/<int:id>", view_func=RentView.as_view("rent", rent_repo))
app.run(debug=True, host="localhost", port=5000)
