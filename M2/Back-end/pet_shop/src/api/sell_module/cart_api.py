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
def create_cart(id_user, role):
    id_cart = db_cart_manager.insert_data(id_user)
    return jsonify(message="Cart created", id=id_cart), 201


@cart_bp.route("/me/carts", methods=["GET"])
@role_required(["admin", "user"])
@validate_fields(optional=["id_cart", "state"])
def get_cart(id_user, role, id_cart:int|None=None, state:str|None=None):
    carts = db_cart_manager.get_data(id_user, id_cart, state)
    return jsonify(carts=carts), 200


@cart_bp.route("/cart", methods=["GET"])
@role_required(["admin", "user"])
def get_current_cart(id_user, role):
    cart = db_cart_manager.get_active_cart(id_user)
    return jsonify(cart=cart), 200


@cart_bp.route("/me/carts/<id_cart>", methods=["PUT"])
@role_required(["admin", "user"])
def update_cart(id_user, role, id_cart):
    db_cart_manager.update_data(id_cart, "active", id_user)
    return jsonify(message="Cart updated"), 200


@cart_bp.route("/me/carts/<id_cart>", methods=["DELETE"])
@role_required(["admin", "user"])
def delete_cart(id_user, role, id_cart):
    db_cart_manager.delete_data(id_cart, id_user)
    return jsonify(message="Cart Deleted"), 200
