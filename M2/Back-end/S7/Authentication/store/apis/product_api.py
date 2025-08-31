from flask import Flask
from flask import jsonify, Response, request
from db.db_product_manager import DbProductManager

app = Flask("products")
db_product_manager = DbProductManager

@app.route('/products', methods=['POST'])
def register_product():
    data = request.get_json()
    product_name = data.get("name")
    product_price = data.get("price")
    product_entry_date=data.get("entry_date")
    product_amount=data.get("amount")
    if (name == None or product_price == None or product_entry_date == None or product_amount==None):
        Response()
    else:
        result=db_product_manager.insert_product(product_name, product_price,product_entry_date, product_amount)
        jsonify({"id":result}),201

@app.route('/products', methods=['GET'])
def get_products():
    results=db_product_manager.get_products()
    jsonify({"products":results}), 200
    

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    pass

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    pass