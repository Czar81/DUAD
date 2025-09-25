from flask import jsonify, Blueprint
from db.db_user_manager import DbUserManager
from db.db_receipt_manager import DbReceiptManager
from verify_input import role_required, require_fields
from encoding import JWT_Manager

user_bp = Blueprint("user", __name__)
db_user_manager = DbUserManager()
db_receipt_manager = DbReceiptManager()
jwt_manager = JWT_Manager()


@user_bp.route("/register", methods=["POST"])
@require_fields("username", "password")
def register(username, password):
    result = db_user_manager.insert_user(username, password)
    user_id = result[0]
    token = JWT_Manager.encode({"id": user_id})
    return jsonify(token=token), 201


@user_bp.route("/login", methods=["POST"])
@require_fields("username", "password")
def login(username, password):
    user_id = db_user_manager.get_user(username, password)
    if user_id == None:
        return jsonify(message="User not exist"), 401
    else:
        token = JWT_Manager.encode({"id": user_id})
        return jsonify(token=token), 200


@user_bp.route("/me", methods=["GET"])
@role_required(["user", "admin"])
def me(user_id):
    user = db_user_manager.get_user_by_id(user_id)
    return jsonify(id=user_id, username=user[1])


@user_bp.route("/me/receipts", methods=["GET"])
@role_required(["user", "admin"])
def get_user_receipt(user_id):
    receipts = db_receipt_manager.get_receipt_by_user_id(user_id)
    return jsonify(receipts=receipts), 200
