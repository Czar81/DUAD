from flask import jsonify, Blueprint
from src.extensions import db_payment_manager
from src.utils import (
    role_required,
    validate_fields,
    register_error_handlers,
)

payment_bp = Blueprint("payment", __name__)
register_error_handlers(payment_bp)

@payment_bp.route("/me/payment", methods=["POST"])
@role_required(["admin","user"])
@validate_fields(required=["type_data","data"])
def register_payment(id_user, type_data, data):
    id_payment=db_payment_manager.insert_data(id_user, type_data, data)
    return jsonify(message="Payment created",data={"id":id_payment}), 201


@payment_bp.route("/me/payment", methods=["GET"])
@role_required(["admin","user"])
@validate_fields(optional=["type_data"])
def get_payment(id_user, role, type_data):
    if role == "user":
        payment = db_payment_manager.get_data(id_user=id_user, type=type_data)
    else:
        payment = db_payment_manager.get_data(type=type_data)
    return jsonify(data=payment), 200


@payment_bp.route("/me/payment/<id_payment>", methods=["GET"])
@role_required(["admin","user"])
def get_payment(id_payment, role, id_user):
    if role == "user":
        payment = db_payment_manager.get_data(id_payment,id_user)
    else:
        payment = db_payment_manager.get_data(id_payment)
    return jsonify(data=payment), 200


@payment_bp.route("/me/payment/<id_payment>", methods=["DELETE"])
@role_required(["admin", "user"])
def delete_payment(id_user, role, id_payment):
    if role == "user":
        db_payment_manager.delete_data(id_payment, id_user)
    else:
        db_payment_manager.delete_data(id_payment)
    return jsonify(message="Payment deleted"), 200
