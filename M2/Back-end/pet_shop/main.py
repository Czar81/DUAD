from src.api.user_module.address_api import address_bp
from src.api.user_module.payment_api import payment_bp
from src.api.user_module.user_api import user_bp
from src.api.sell_module.cart_api import cart_bp
from src.api.sell_module.cart_item_api import cart_items_bp
from src.api.sell_module.product_api import product_bp
from src.api.sell_module.receipt_api import receipt_bp
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