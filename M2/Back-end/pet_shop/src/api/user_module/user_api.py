from flask import jsonify, Blueprint, request
from src.extensions import db_user_manager, jwt_manager
from src.utils import (
    role_required,
    validate_fields,
    register_error_handlers,
)
import os

user_bp = Blueprint("user", __name__)
register_error_handlers(user_bp)


@user_bp.route("/register", methods=["POST"])
@validate_fields(required=["username", "password"])
def register(username, password):
    if request.headers.get("X-ADMIN-TOKEN") == os.getenv("ADMIN_BOOTSTRAP_TOKEN"):
        id_user = db_user_manager.insert_data(username, password, role="admin")
    id_user = db_user_manager.insert_data(username, password)
    token = jwt_manager.encode({"id": id_user})
    return jsonify(token=token), 201


@user_bp.route("/login", methods=["POST"])
@validate_fields(required=["username", "password"])
def login(username, password):
    id_user = db_user_manager.get_user(username, password)
    if id_user is None:
        return jsonify(message="User not found, register first"), 404
    token = jwt_manager.encode({"id": id_user})
    return jsonify(token=token), 200


@user_bp.route("/me", methods=["GET"])
@role_required(["user", "admin"])
def me(id_user, role):
    myself = db_user_manager.get_data(id_user)
    return jsonify(user=myself), 200


@user_bp.route("/me", methods=["PUT"])
@role_required(["admin", "user"])
@validate_fields(optional=["username", "password", "new_role"])
def update_profile(id_user, role, username:str|None=None, password:str|None=None, new_role:str|None=None):
    if role == "admin":
        db_user_manager.update_data(id_user, username, password, new_role)
    else:
        db_user_manager.update_data(id_user, username, password)
    return jsonify({"message": "User updated"}), 200


@user_bp.route("/me", methods=["DELETE"])
@role_required(["admin", "user"])
def delete_profile(id_user, role):
    db_user_manager.delete_data(id_user)
    return jsonify(message="User deleted"), 200
