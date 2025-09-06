from flask import Flask
from flask import jsonify, request
from db.db_receipt_manager import DbReceiptManager

app = Flask(__name__)
db_receipt_manager = DbReceiptManager()


@app.route("/sales", methods=["POST"])
def register_receipt():
    data = request.get_json()
    id_user = data.get("id_user")
    id_product = data.get("id_product")
    amount = data.get("amount")
    if id_user == None or id_product == None or amount == None:
        return None
    else:
        db_receipt_manager.create_receipt(id_user, id_product, amount)
