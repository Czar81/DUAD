from flask import jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from src.db.sell_module.db_product_manager import DbProductManager
from src.utils import APIException, role_required, CacheManager, validate_fields

product_bp = Blueprint("product", __name__)
db_product_manager = DbProductManager()
cache_manager = CacheManager()
key_global = "getProducts-all"


@product_bp.route("products", methods=["POST"])
def register_product():
    pass


@product_bp.route("products", methods=["GET"])
def get_products():
    pass


@product_bp.route("products/<id_product>", methods=["GET"])
def get_product(id_product):
    key = f"getProduct:{id_product}"
    try:
        result = __get_cache_if_exist(key, id_product)
        return jsonify({"products": result}), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(error=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("products/<id_product>", methods=["PUT"])
def update_product():
    pass


@product_bp.route("products/<id_product>", methods=["DELETE"])
def delete_product():
    pass


def __get_cache_if_exist(
    key,
    id_product: int | None = None,
    sku: str | None = None,
    name: str | None = None,
    price: int | None = None,
    amount: int | None = None,
):
    result = cache_manager.get_data(key)
    if result is None:
        result = db_product_manager.get_data(id_product, sku, name, price, amount)
        if result is None:
            raise APIException("Could not find any product with params", 404)
        cache_manager.store_data(key, result)
    return result
