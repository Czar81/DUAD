from flask import Blueprint, jsonify
from src.extensions import db_cart_item_manager
from src.utils import (
    role_required,
    validate_fields,
    register_error_handlers,
)

cart_items_bp = Blueprint("cart_items", __name__)
register_error_handlers(cart_items_bp)


@cart_items_bp.route("/add-item", methods=["POST"])
@role_required(["admin", "user"])
@validate_fields(required=["id_cart","id_product", "amount"])
def create_cart_item(id_cart,id_product, amount, id_user, role):
    id_item = db_cart_item_manager.insert_data(id_cart,id_product, amount, id_user)
    return jsonify(id_item=id_item, message="Item added"), 201


@cart_items_bp.route("/modify-item", methods=["PUT"])
@validate_fields(required=["amount"])
@role_required(["admin", "user"])
def update_cart_item(id_user, amount, id_cart_item):
    db_cart_item_manager.update_data(id_cart_item, amount, id_user)
    return jsonify(message="Amount updated"), 200


@cart_items_bp.route("/remove-item", methods=["DELETE"])
@role_required(["admin", "user"])
def delete_cart_item(id_user, id_cart_item):
    db_cart_item_manager.delete_data(id_cart_item, id_user)
    return jsonify(message="Item deleted"), 200
