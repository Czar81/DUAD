from flask import jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from src.db.sell_module.db_product_manager import DbProductManager
from src.utils import (
    APIException,
    role_required,
    CacheManager,
    validate_fields,
    generate_cache_based_filters,
    generate_cache_key,
    register_error_handlers,
)

product_bp = Blueprint("product", __name__)
register_error_handlers(product_bp)
db_product_manager = DbProductManager()
cache_manager = CacheManager()


@product_bp.route("products", methods=["POST"])
@role_required(["admin"])
@validate_fields(required=["sku", "name", "price", "amount"])
def register_product(sku, name, price, amount):
    id_product = db_product_manager.insert_data(sku, name, price, amount)
    cache_manager.delete_data_with_pattern("getProducts:")
    return jsonify({"id": f"Product created id{id_product}"}), 201


@product_bp.route("products", methods=["GET"])
@validate_fields(optional=["id_product", "sku", "name", "price", "amount"])
def get_products(**filters):
    key = generate_cache_based_filters("getProducts", filters)
    result = __get_cache_if_exist(key, **filters)
    return jsonify({"products": result}), 200


@product_bp.route("products/<id_product>", methods=["GET"])
def get_product(id_product):
    try:
        id_product = int(id_product)
    except ValueError:
        return jsonify(error="id_product must be an integer"), 400
    key = generate_cache_key("getProduct", id_product=id_product)
    result = __get_cache_if_exist(key, id_product=int(id_product))
    return jsonify({"product": result}), 200


@product_bp.route("products/<id_product>", methods=["PUT"])
@role_required(["admin"])
@validate_fields(optional=["sku", "name", "price", "amount"])
def update_product(id_product, **filters):
    try:
        id_product = int(id_product)
    except ValueError:
        return jsonify(error="id_product must be an integer"), 400
    filters["id_product"] = id_product
    key = generate_cache_key("getProduct", id_product=id_product)
    db_product_manager.update_data(**filters)
    cache_manager.delete_data(key)
    cache_manager.delete_data_with_pattern("getProducts:")
    return jsonify({"message": "Product Updated"}), 200


@product_bp.route("products/<id_product>", methods=["DELETE"])
@role_required(["admin"])
def delete_product(id_product):
    try:
        id_product = int(id_product)
    except ValueError: 
        return jsonify(error="id_product must be an integer"), 400
    key = generate_cache_key("getProduct", id_product=id_product)
    db_product_manager.delete_data(id_product)
    cache_manager.delete_data(key)
    cache_manager.delete_data_with_pattern("getProducts:")
    return jsonify({"message": "Product Deleted"}), 200

def __get_cache_if_exist(key, **search_params):
    result = cache_manager.get_data(key)
    if result is None:
        result = db_product_manager.get_data(**search_params)
        if result is None:
            raise APIException("Could not find any product with params", 404)
        cache_manager.store_data(key, result)
    return result
