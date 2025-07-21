from flask import Flask
from api.user_api import UserView
from scripts.database.pg_manager import PgManager

app = Flask(__name__)
db_manager = PgManager(
    db_name="postgres", user="postgres", password="postgres", host="localhost"
)
app.add_url_rule("/user/<int:id>", view_func=UserView.root.as_view("user", db_manager))
