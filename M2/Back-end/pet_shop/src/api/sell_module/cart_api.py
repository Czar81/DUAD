from flask import Blueprint, jsonify
from src.extensions import db_cart_manager
from src.utils import (
    APIException,
    role_required,
    validate_fields,
    register_error_handlers,
)

cart_bp = Blueprint("cart", __name__)
register_error_handlers(cart_bp)


@cart_bp.route("/me/carts", methods=["POST"])
@role_required(["admin", "user"])
@validate_fields(optional=["state"])
def create_cart(id_user, role, state):
    if role == "user":
        id_cart = db_cart_manager.insert_data(id_user)
    else:
        id_cart = db_cart_manager.insert_data(id_user, state)
    return jsonify(message="Cart created", data={"id": id_cart}), 201


@cart_bp.route("/me/carts", methods=["GET"])
@role_required(["admin", "user"])
@validate_fields(optional=["id_cart", "state"])
def get_cart(id_user, id_cart, state):
    receipts = db_cart_manager.get_data(id_cart, id_user, state)
    return jsonify(data=receipts), 200


@cart_bp.route("/cart", methods=["GET"])
@role_required(["admin", "user"])
@validate_fields(required=["id_cart"])
def get_current_cart(id_cart):
    receipts = db_cart_manager.get_data(id_cart)
    return jsonify(data=receipts), 200


@cart_bp.route("/me/carts/<id_cart>", methods=["PUT"])
@role_required(["admin", "user"])
def update_cart(id_user, role, id_cart):
    if role == "user":
        db_cart_manager.update_data(id_cart, "active", id_user)
    else:
        db_cart_manager.update_data(id_cart, "active")
    return jsonify(message="Cart updated"), 200


@cart_bp.route("/me/carts/<id_cart>", methods=["DELETE"])
@role_required(["admin", "user"])
def delete_cart(id_user, role, id_cart):
    if role == "user":
        db_cart_manager.delete_data(id_cart, id_user)
    else:
        db_cart_manager.delete_data(id_cart)
    return jsonify(message="Cart deleted"), 200
