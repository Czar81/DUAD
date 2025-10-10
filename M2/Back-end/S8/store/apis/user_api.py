from flask import jsonify, Blueprint
from db.db_user_manager import DbUserManager
from db.db_receipt_manager import DbReceiptManager
from sqlalchemy.exc import SQLAlchemyError
from utils import JWT_Manager, APIException, role_required, require_fields, CacheManager

user_bp = Blueprint("user", __name__)
db_user_manager = DbUserManager()
db_receipt_manager = DbReceiptManager()
jwt_manager = JWT_Manager()
cache_manager = CacheManager()


@user_bp.route("/user/register", methods=["POST"])
@require_fields("username", "password")
def register(username, password):
    try:
        result = db_user_manager.insert_user(username, password)
        user_id = result[0]
        token = jwt_manager.encode({"id": user_id})
        return jsonify(token=token), 201
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@user_bp.route("/user/login", methods=["POST"])
@require_fields("username", "password")
def login(username, password):
    try:
        user_id = db_user_manager.get_user(username, password)
        if user_id == None:
            return jsonify(message="User not exist"), 401
        else:
            token = jwt_manager.encode({"id": user_id})
            return jsonify(token=token), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@user_bp.route("/me", methods=["GET"])
@role_required(["user", "admin"])
def me(user_id):
    try:
        user = db_user_manager.get_user_by_id(user_id)
        return jsonify(id=user_id, username=user[1]), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@user_bp.route("/me/receipts", methods=["GET"])
@role_required(["user", "admin"])
def get_user_receipt(user_id):
    try:
        receipts = __get_cache_if_exist(f"getReceipt:{id_user}", user_id)
        return jsonify(receipts=receipts), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500

def __get_cache_if_exist(key, id):
    result = cache_manager.get_data(key)
    if result is None:
        result = db_receipt_manager.get_receipt_by_user_id(id)
        cache_manager.store_data(key, result)
    return result