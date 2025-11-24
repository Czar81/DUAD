from src.api import (
    address_bp,
    cart_bp,
    user_bp,
    payment_bp,
    product_bp,
    receipt_bp,
    cart_items_bp,
)
from flask import Flask
from dotenv import load_dotenv
from src.extensions import tm
from os import environ

load_dotenv()

app = Flask("Store-service")

if __name__ == "__main__":
    tm.create_tables()
    app.register_blueprint(product_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(cart_items_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(receipt_bp)
    app.run(
        host=environ.get("HOST_API"),
        port=environ.get("PORT_API"),
        debug=environ.get("DEBUG_MODE"),
    )
