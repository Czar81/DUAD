from flask import jsonify, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from src.db.sell_module.db_product_manager import DbProductManager
from src.utils import APIException, general_data_validation, role_required, CacheManager

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

@product_bp.route("products/<product_id>", methods=["PUT"])
def update_product():
    pass

@product_bp.route("products/<product_id>", methods=["DELETE"])
def delete_product():
    pass
