from flask import Flask
from db.tables_manager import TablesManager
from apis.product_api import product_bp
from apis.receipt_api import receipt_bp
from apis.user_api import user_bp

app = Flask("Store-service")

if __name__ == "__main__":
    # Add trys except with HTTPs code
    TablesManager.create_tables()
    app.register_blueprint(product_bp)  
    app.register_blueprint(user_bp)  
    app.register_blueprint(receipt_bp)  
    app.run(host="localhost", port=5000, debug=True)
