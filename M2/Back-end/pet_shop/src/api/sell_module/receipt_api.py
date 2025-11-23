from flask import jsonify, Blueprint
from src.db.sell_module.db_receipt_manager import DbReceiptManager
from src.utils import (
    APIException,
    role_required,
    validate_fields,
    register_error_handlers,
)

receipt_bp = Blueprint("receipt", __name__)
register_error_handlers(receipt_bp)
db_receipt_manager = DbReceiptManager()

@receipt_bp.route("me/receipt", methods=["POST"])
@role_required(["admin", "user"])
@validate_fields(required=["id_cart", "id_address", "id_payment"], optional=["state"])
def create_receipt(id_cart, id_address, id_payment, id_user, role, state):
    if role == "user":
        db_receipt_manager.create_receipt(id_cart, id_address, id_payment, id_user=id_user)
    else:
        db_receipt_manager.create_receipt(id_cart, id_address, id_payment, state,id_user)
    return jsonify(message="Receipt created"), 201


@receipt_bp.route("me/receipt", methods=["GET"])
@role_required(["admin", "user"])
@validate_fields(optional=["id_cart", "id_address", "id_payment", "state", "entry_date"])
def get_receipt(**filters):
    receipts=db_receipt_manager.get_data(**filters)
    return jsonify(data=receipts), 200

@receipt_bp.route("me/receipt/<id_receipt>", methods=["GET"])
@role_required(["admin", "user"])
def get_receipt(id_receipt):
    receipts=db_receipt_manager.get_data(id_receipt)
    return jsonify(data=receipts), 200

@receipt_bp.route("me/receipt", methods=["POST"])
@role_required(["admin", "user"])
@validate_fields(required=["id_receipt", "id_user"])
def return_receipt(role, id_user, id_receipt):
    if role == "user":
        db_receipt_manager.return_receipt(id_receipt, id_user)
    else:
        db_receipt_manager.return_receipt(id_receipt, id_user)
    return jsonify(message="Receipt returned"), 200
    