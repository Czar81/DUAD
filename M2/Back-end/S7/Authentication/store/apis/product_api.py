from flask import jsonify, Blueprint
from db.db_product_manager import DbProductManager
from verify_input import general_data_validation, role_required
from sqlalchemy.exc import SQLAlchemyError
from api_exception import APIException

product_bp = Blueprint("product", __name__)
db_product_manager = DbProductManager()


@product_bp.route("/products", methods=["POST"])
@general_data_validation(["admin"], "name", "price", "amount")
def register_product(name, price, amount):
    try:
        id_returned = db_product_manager.insert_product(name, price, amount)
        return jsonify({"id": str(id_returned)}), 201
    except SQLAlchemyError as e:
        jsonify(error=f"Internal database error: {e}"), 500
    except Exception as e:
        jsonify(error=f"An unexpected error occurred"), 500
    except APIException as e:
        jsonify(error=e), e.status_code


@product_bp.route("/products", methods=["GET"])
def get_products():
    try:
        results = db_product_manager.get_products()
        return jsonify({"products": results}), 200
    except SQLAlchemyError as e:
        jsonify(error=f"Internal database error: {e}"), 500
    except Exception as e:
        jsonify(error=f"An unexpected error occurred"), 500
    except APIException as e:
        jsonify(error=e), e.status_code


@product_bp.route("/products/<product_id>", methods=["PUT"])
@general_data_validation(["admin"], "name", "price", "amount")
def update_product(product_id, name, price, amount):
    try:
        db_product_manager.update_product(int(product_id), name, price, amount)
        return jsonify({"message": "Product Updated"}), 200
    except SQLAlchemyError as e:
        jsonify(error=f"Internal database error: {e}"), 500
    except Exception as e:
        jsonify(error=f"An unexpected error occurred"), 500
    except APIException as e:
        jsonify(error=e), e.status_code


@product_bp.route("/products/<product_id>", methods=["DELETE"])
@role_required(["admin"])
def delete_product(product_id):
    try:
        db_product_manager.delete_product(product_id)
        return jsonify({"message": "Product Deleted"}), 200
    except SQLAlchemyError as e:
        jsonify(error=f"Internal database error: {e}"), 500
    except Exception as e:
        jsonify(error=f"An unexpected error occurred"), 500
    except APIException as e:
        jsonify(error=e), e.status_code
