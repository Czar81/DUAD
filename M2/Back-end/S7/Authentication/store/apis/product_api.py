from flask import Flask
from flask import jsonify, request
from db.db_product_manager import DbProductManager
from verify_input import general_data_validation, role_required

app = Flask(__name__)
db_product_manager = DbProductManager()


@app.route("/products", methods=["POST"])
@general_data_validation(["admin"], "name", "price", "amount")
def register_product(name, price, amount):
    id_returned = db_product_manager.insert_product(name, price, amount)
    return jsonify({"id": str(id_returned)}), 201


@app.route("/products", methods=["GET"])
@role_required(["admin", "user"])
def get_products():
    results = db_product_manager.get_products()
    return jsonify({"products": results}), 200


@app.route("/products/<product_id>", methods=["PUT"])
@general_data_validation(["admin"], "name", "price", "amount")
def update_product(product_id,name,price,amount):
    db_product_manager.update_product(int(product_id), name, price, amount)
    return jsonify({"message": "Product Updated"}), 200


@app.route("/products/<product_id>", methods=["DELETE"])
@role_required(["admin"])
def delete_product(product_id):
    db_product_manager.delete_product(product_id)
    return jsonify({"message": "Product Deleted"}), 200


def start_product_api():
    app.run(host="localhost", port=5000, debug=True)
