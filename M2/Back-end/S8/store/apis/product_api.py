from flask import jsonify, Blueprint
from db.db_product_manager import DbProductManager
from sqlalchemy.exc import SQLAlchemyError
from redis import RedisError
from utils import APIException, general_data_validation, role_required, CacheManager

product_bp = Blueprint("product", __name__)
db_product_manager = DbProductManager()
cache_manager = CacheManager()


@product_bp.route("/products", methods=["POST"])
@general_data_validation(["admin"], "name", "price", "amount")
def register_product(id_user, name, price, amount):
    key = "getProducts-all"
    try:
        id_returned = db_product_manager.insert_product(name, price, amount)
        cache_manager.delete_data(key)
        return jsonify({"id": str(id_returned)}), 201
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("/products", methods=["GET"])
def get_products():
    key = "getProducts-all"
    try:
        result = __get_cache_if_exist(key)
        return jsonify({"products": result}), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(errror=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("/products/<product_id>", methods=["GET"])
def get_product_by_id(product_id):
    key = f"getProduct:{product_id}"
    try:
        result = __get_cache_if_exist(key, product_id, by_id=True)
        return jsonify({"product": result}), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(errror=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("/products/<product_id>", methods=["PUT"])
@general_data_validation(["admin"], "name", "price", "amount")
def update_product(id_user, product_id, name, price, amount):
    key = f"getProduct:{product_id}"
    try:
        db_product_manager.update_product(int(product_id), name, price, amount)
        cache_manager.delete_data(key)
        return jsonify({"message": "Product Updated"}), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(errror=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("/products/<product_id>", methods=["DELETE"])
@role_required(["admin"])
def delete_product(id_user, product_id):
    key = f"getProduct:{product_id}"
    try:
        db_product_manager.delete_product(product_id)
        cache_manager.delete_data(key)
        return jsonify({"message": "Product Deleted"}), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(errror=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


def __get_cache_if_exist(key, id=None, by_id=False):
    result = cache_manager.get_data(key)
    if result is None:
        if by_id and id is not None:
            result = db_product_manager.get_product_by_id(id)
        else:
            result = db_product_manager.get_products()
        cache_manager.store_data(key, result)
    return result
