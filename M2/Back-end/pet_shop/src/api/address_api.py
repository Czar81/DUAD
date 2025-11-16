from flask import jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from src.db.user_module.db_address_manager import DbAddressManager
from src.utils import (
    APIException,
    role_required,
    validate_fields,
    register_error_handlers,
)

address_bp = Blueprint("address", __name__)
register_error_handlers(address_bp)
db_address_manager = DbAddressManager()


@address_bp.route("<name>/address", methods=["POST"])
@role_required(["admin","user"])
@validate_fields(required=["location"])
def register_address(id_user, location):
    db_address_manager.insert_data(id_user, location)
    return jsonify(message="Address created"), 201


@address_bp.route("<name>/address", methods=["GET"])
@role_required(["admin","user"])
def get_address(id_user, role):
    if role == "user":
        address = db_address_manager.get_data(id_user=id_user)
    else:
        address = db_address_manager.get_data()
    return jsonify(data=address), 200


@address_bp.route("<name>/address/<id_address>", methods=["GET"])
@role_required(["admin","user"])
def get_address(id_address,role, id_user):
    if role == "user":
        address = db_address_manager.get_data(id_address,id_user)
    else:
        address = db_address_manager.get_data(id_address)
    return jsonify(data=address), 200


@address_bp.route("<name>/address/<id_address>", methods=["PUT"])
@role_required(["admin","user"])
@validate_fields(required=["location"])
def update_address(id_user, role, id_address, location):
    if role == "user":
        db_address_manager.update_data(id_address, location, id_user)
    else:
        db_address_manager.update_data(id_address, location)
    return jsonify(message="Address updated"), 200


@address_bp.route("<name>/address/<id_address>", methods=["DELETE"])
@role_required(["admin", "role"])
def delete_address(id_user, role, id_address):
    if role == "user":
        db_address_manager.delete_data(id_address, id_user)
    else:
        db_address_manager.delete_data(id_address)
    return jsonify(message="Address deleted"), 200
