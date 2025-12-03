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
import pytest


@pytest.fixture
def client():
    app = Flask("Store-service")
    app.config["TESTING"] = True
    app.register_blueprint(address_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(receipt_bp)
    app.register_blueprint(cart_items_bp)
    with app.test_client() as client:
        yield client


@pytest.fixture
def get_token_user(client):
    response = client.post(
        "/register", json={"username": "TestUser", "password": "12345"}
    )
    response = client.post("/login", json={"username": "TestUser", "password": "12345"})
    return response.json["token"]
