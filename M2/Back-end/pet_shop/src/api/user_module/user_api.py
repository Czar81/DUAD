from flask import jsonify, Blueprint
from src.db.user_module.db_user_manager import DbUserManager
from src.utils import (
    role_required,
    validate_fields,
    register_error_handlers,
    JWT_Manager
)

user_bp = Blueprint("user", __name__)
register_error_handlers(user_bp)
db_user_manager = DbUserManager()
jwt_manager = JWT_Manager()


@user_bp.route("register", methods=["POST"])
@role_required(["user", "admin"])
@validate_fields(required=["name", "password"])
def register(name, password):
    id_user = db_user_manager.insert_data(name, password, "user")
    token = jwt_manager.encode({"id": id_user})
    return jsonify(token=token), 201


@user_bp.route("login", methods=["POST"])
@role_required(["user", "admin"])
@validate_fields(required=["name", "password"])
def login(name, password):
    id_user = db_user_manager.get_data(name, password)
    token = jwt_manager.encode({"id": id_user})
    return jsonify(token=token), 200


@user_bp.route("me", methods=["GET"])
@role_required(["user", "admin"])
def me(id_user):
    myself = db_user_manager.get_data(id_user)
    return jsonify(user=myself), 200


@user_bp.route("me", methods=["PUT"])
@role_required(["admin", "user"])
@validate_fields(optional=["name", "password", "role"])
def update_product(id_user, role, **filters):
    if role == "admin":
        db_user_manager.update_data(id_user, **filters)
    else:
        db_user_manager.update_data(id_user, filters["name"], filters["password"])
    return jsonify({"message": "User updated"}), 200


@user_bp.route("me", methods=["DELETE"])
@role_required(["admin", "user"])
def delete_product(id_user):
    db_user_manager.delete_data(id_user)
    return jsonify(message="User deleted"), 200
