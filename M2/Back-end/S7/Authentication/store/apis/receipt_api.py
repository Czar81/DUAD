from flask import Flask
from flask import jsonify, request
from db.db_receipt_manager import DbReceiptManager
from encoding import JWT_Manager

app = Flask(__name__)
db_receipt_manager = DbReceiptManager()
jwt_manager=JWT_Manager("MyNameIsJeff","HS256")

@app.route("/receipts", methods=["POST"])
def register_receipt():
    data = request.get_json()
    id_user = data.get("id_user")
    id_product = data.get("id_product")
    amount = data.get("amount")
    if id_user == None or id_product == None or amount == None:
        return None
    else:
        db_receipt_manager.create_receipt(id_user, id_product, amount)
        return jsonify({"message":"Receipt created successfully"}),201


def start_receipt_api():
    app.run(host="localhost",port=5001, debug=True)