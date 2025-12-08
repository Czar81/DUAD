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
from os import getenv

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


@pytest.fixture
def get_token_admin(client):
    response = client.post(
        "/register",
        json={"username": "admin232", "password": "fds67tf67dstf67sdf687sd"},
        headers={"X-ADMIN-TOKEN": getenv("ADMIN_BOOTSTRAP_TOKEN")},
    )
    response = client.post("/login", json={"username": "admin232", "password": "fds67tf67dstf67sdf687sd"})
    return response.json["token"]

@pytest.fixture(autouse=True)
def clean_db():
    from sqlalchemy import text
    from src.extensions import tm

    engine = tm.engine
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM user"))