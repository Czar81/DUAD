from flask import Flask
from flask import jsonify, Response, request
from db.db_product_manager import DbProductManager

app = Flask(__name__)
db_product_manager = DbProductManager()


@app.route("/products/register", methods=["POST"])
def register_product():
    data = request.get_json()
    product_name = data.get("name")
    product_price = data.get("price")
    product_amount = data.get("amount")
    if product_name == None or product_price == None or product_amount == None:
        return jsonify({"message": "Missing fields in request"}), 400
    else:
        id_returned = db_product_manager.insert_product(
            product_name, product_price, product_amount
        )
        return jsonify({"id": str(id_returned)}), 201


@app.route("/products", methods=["GET"])
def get_products():
    results = db_product_manager.get_products()
    return jsonify({"products": results}), 200


@app.route("/products/update/<product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    new_name = data.get("name")
    new_price = data.get("price")
    new_amount = data.get("amount")
    if new_name == None or new_price == None or new_amount == None:
        return jsonify({"message": "Missing fields in request"}), 400
    else:
        db_product_manager.update_product(
            int(product_id), new_name, new_price, new_amount
        )
        return jsonify({"message": "Product Updated"}), 200


@app.route("/products/delete/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    db_product_manager.delete_product(product_id)
    return jsonify({"message": "Product Deleted"}), 200


def start_product_api():
    app.run(host="localhost",port=5000, debug=True)