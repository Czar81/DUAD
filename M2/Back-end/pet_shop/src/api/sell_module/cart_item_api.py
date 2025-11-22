from flask import Blueprint, jsonify
from src.db.sell_module.db_cart_item_manager import DbCartItemsManager
from src.utils import (
    APIException,
    role_required,
    validate_fields,
    register_error_handlers,
)

cart_items_bp = Blueprint("cart_items", __name__)
register_error_handlers(cart_items_bp)
db_cart_item_manager = DbCartItemsManager()


@cart_items_bp.route("add-item", methods=["POST"])
@role_required(["admin", "user"])
@validate_fields(required=["id_cart","id_product", "amount"])
def create_cart_item(id_cart,id_product, amount, id_user):
    db_cart_item_manager.insert_data(id_cart,id_product, amount, id_user)
    return jsonify(message="Item added"), 201


@cart_items_bp.route("car/modify-item", methods=["PUT"])
@role_required(["admin", "user"])
def update_cart_item(id_user, amount, id_cart_item):
    db_cart_item_manager.update_data(id_cart_item, amount, id_user)
    return jsonify(message="Amounr updated"), 200


@cart_items_bp.route("car/remove-item", methods=["DELETE"])
@role_required(["admin", "user"])
def delete_cart_item(id_user, id_cart_item):
    db_cart_item_manager.delete_data(id_cart_item, id_user)
    return jsonify(message="Item deleted"), 200
