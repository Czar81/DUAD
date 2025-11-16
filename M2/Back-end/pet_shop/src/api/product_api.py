from flask import jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from src.db.sell_module.db_product_manager import DbProductManager
from src.utils import (
    APIException,
    role_required,
    CacheManager,
    validate_fields,
    generate_cache_based_filters,
)

product_bp = Blueprint("product", __name__)
db_product_manager = DbProductManager()
cache_manager = CacheManager()


@product_bp.route("products", methods=["POST"])
@role_required(["admin"])
@validate_fields(required=["sku", "name", "price", "amount"])
def register_product(sku, name, price, amount):
    try:
        id_product = db_product_manager.insert_data(sku, name, price, amount)
        cache_manager.delete_data_with_pattern("getProducts:")
        return jsonify({"id": f"Product created id{id_product}"}), 200
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(error=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("products", methods=["GET"])
@validate_fields(optional=["id_product", "sku", "name", "price", "amount"])
def get_products(**filters):
    try:
        key = generate_cache_based_filters("getProducts", filters)
        result = __get_cache_if_exist(key, **filters)
        return jsonify({"products": result}), 200
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(error=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("products/<id_product>", methods=["GET"])
def get_product(id_product):
    try:
        key = generate_cache_key("getProduct", id_product=id_product)
        result = __get_cache_if_exist(key, id_product=int(id_product))
        return jsonify({"product": result}), 200
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(error=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("products/<id_product>", methods=["PUT"])
@role_required(["admin"])
@validate_fields(optional=["sku", "name", "price", "amount"])
def update_product(id_product,**filters):
    try:
        filters['id_product'] = id_product
        key = generate_cache_key("getProduct", id_product=id_product)
        db_product_manager.update_data(**filters)
        cache_manager.delete_data(key)
        cache_manager.delete_data_with_pattern("getProducts:")
        return jsonify({"message": "Product Updated"}), 200
    except SQLAlchemyError as e:
        return jsonify(error=f"Internal database error: {e}"), 500
    except APIException as e:
        return jsonify(error=str(e)), e.status_code
    except RecursionError as e:
        return jsonify(error=f"An unexpected error occurred with redis: {e}"), 500
    except Exception as e:
        return jsonify(error=f"An unexpected error occurred: {e}"), 500


@product_bp.route("products/<id_product>", methods=["DELETE"])
def delete_product():
    pass


def __get_cache_if_exist(key, **search_params):
    result = cache_manager.get_data(key)
    if result is None:
        result = db_product_manager.get_data(**search_params)
        if result is None:
            raise APIException("Could not find any product with params", 404)
        cache_manager.store_data(key, result)
    return result
