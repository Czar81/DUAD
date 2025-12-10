from flask import jsonify, Blueprint
from src.extensions import db_address_manager
from src.utils import (
    role_required,
    validate_fields,
    register_error_handlers,
)

address_bp = Blueprint("address", __name__)
register_error_handlers(address_bp)


@address_bp.route("/me/address", methods=["POST"])
@role_required(["admin", "user"])
@validate_fields(required=["location"])
def register_address(id_user, role, location):
    id_address = db_address_manager.insert_data(id_user, location)
    return jsonify(message="Address created", id=id_address), 201


@address_bp.route("/me/address", methods=["GET"])
@role_required(["admin", "user"])
def get_address(id_user, role):
    if role == "user":
        address = db_address_manager.get_data(id_user=id_user)
    else:
        address = db_address_manager.get_data()
    return jsonify(data=address), 200


@address_bp.route("/me/address/<id_address>", methods=["GET"])
@role_required(["admin", "user"])
def get_single_address(id_address, role, id_user):
    if role == "user":
        address = db_address_manager.get_data(id=id_address, id_user=id_user)
    else:
        address = db_address_manager.get_data(id=id_address)
    return jsonify(data=address), 200


@address_bp.route("/me/address/<id_address>", methods=["PUT"])
@role_required(["admin", "user"])
@validate_fields(required=["location"])
def update_address(id_user, role, id_address, location):
    if role == "user":
        db_address_manager.update_data(id_address, location, id_user)
    else:
        db_address_manager.update_data(id_address, location)
    return jsonify(message="Address updated"), 200


@address_bp.route("/me/address/<id_address>", methods=["DELETE"])
@role_required(["admin", "user"])
def delete_address(id_user, role, id_address):
    if role == "user":
        db_address_manager.delete_data(id_address, id_user)
    else:
        db_address_manager.delete_data(id_address)
    return jsonify(message="Address deleted"), 200
