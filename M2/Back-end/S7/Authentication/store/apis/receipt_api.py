from flask import Flask
from flask import jsonify
from db.db_receipt_manager import DbReceiptManager
from verify_input import general_data_validation
from encoding import JWT_Manager

app = Flask(__name__)
db_receipt_manager = DbReceiptManager()
jwt_manager = JWT_Manager()


@app.route("/receipts", methods=["POST"])
@general_data_validation(["user","admin"], "id_user", "id_product", "amount")
def register_receipt(id_user, id_product, amount):
    db_receipt_manager.create_receipt(id_user, id_product, amount)
    return jsonify(message="Receipt created successfully"), 201


def start_receipt_api():
    app.run(host="localhost", port=5001, debug=True)
