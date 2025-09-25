from flask import jsonify, Blueprint
from db.db_receipt_manager import DbReceiptManager
from verify_input import general_data_validation
from sqlalchemy.exc import SQLAlchemyError
from api_exception import APIException

receipt_bp = Blueprint("receipt", __name__)
db_receipt_manager = DbReceiptManager()


@receipt_bp.route("/receipts", methods=["POST"])
@general_data_validation(["user", "admin"], "id_user", "id_product", "amount")
def register_receipt(id_user, id_product, amount):
    try:
        db_receipt_manager.create_receipt(id_user, id_product, amount)
        return jsonify(message="Receipt created successfully"), 201
    except SQLAlchemyError as e:
        jsonify(error=f"Internal database error: {e}"), 500
    except Exception as e:
        jsonify(error=f"An unexpected error occurred"), 500
    except APIException as e:
        jsonify(error=e), e.status_code
