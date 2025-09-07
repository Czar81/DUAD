from flask import Flask
from flask import jsonify, Response, request
from db.db_user_manager import DbUserManager
from db.db_receipt_manager import DbReceiptManager
from verify_user import role_required, require_user_fields
from encoding import JWT_Manager

app = Flask("user-service")
db_user_manager = DbUserManager()
db_receipt_manager = DbReceiptManager()

@app.route("/register", methods=["POST"])
@require_user_fields("username", "password")
def register(username, password):
    result = db_user_manager.insert_user(username, password)
    user_id = result[0]
    token = JWT_Manager.encode({"id": user_id})
    return jsonify(token=token),201


@app.route("/login", methods=["POST"])
@require_user_fields("username", "password")
def login(username, password):
    result = db_user_manager.get_user(username, password)
    if result == None:
        return jsonify(message="User not exist"), 401
    else:
        user_id = result[0]
        token = JWT_Manager.encode({"id": user_id})
        return jsonify(token=token),200


@app.route("/me", methods=["GET"])
@role_required(["user","admin"])
def me(user_id):
    user = db_user_manager.get_user_by_id(user_id)
    return jsonify(id=user_id, username=user[1])


@app.route("/me/receipts", methods=["GET"])
@role_required(["user","admin"])
def get_user_receipt(user_id):
    receipts = db_receipt_manager.get_receipt_by_user_id(user_id)
    return jsonify(receipts = receipts), 200


def start_user_api():
    app.run(host="localhost", port=5002, debug=True)
