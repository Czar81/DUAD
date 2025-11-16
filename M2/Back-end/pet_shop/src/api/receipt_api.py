from flask import jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
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

@receipt_bp.route("<name>/receipt", methods=["POST"])
@role_required(["admin", "user"])
@validate_fields(required=["id_cart", "id_address", "id_payment"], optional=["state"])
def create_receipt(id_cart, id_address, id_payment, id_user, role, state):
    if role == "user":
        db_receipt_manager.create_receipt(id_cart, id_address, id_payment, id_user=id_user)
    else:
        db_receipt_manager.create_receipt(id_cart, id_address, id_payment, state,id_user)
    return jsonify(message="Receipt created"), 201


@receipt_bp.route("<name>/receipt", methods=["GET"])
@role_required(["admin", "user"])
@validate_fields(required=["id_user","id_cart", "id_address", "id_payment", "state", entry_date])
def get_receipt(role, **filters):
    if role == "user":
        receipts=db_receipt_manager.get_data(**filters)
    else:
        receipts=db_receipt_manager.get_data(**filters)
    return jsonify(data=receipts), 200


@receipt_bp.route("<name>/receipt", methods=["POST"])
@role_required(["admin", "user"])
@validate_fields(required=["id_receipt", "id_user"])
def return_receipt(role, id_user, id_receipt):
    if role == "user":
        db_receipt_manager.return_receipt(id_receipt, id_user)
    else:
        db_receipt_manager.return_receipt(id_receipt, id_user)
    return jsonify(message="Receipt returned"), 200
    