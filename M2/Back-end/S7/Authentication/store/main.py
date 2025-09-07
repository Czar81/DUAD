from apis.product_api import start_product_api
from apis.receipt_api import start_receipt_api
from apis.user_api import start_user_api
from tables_manager import TablesManager

if __name__=="__main__":
    TablesManager.create_tables()
    start_user_api()
    start_product_api()
    start_receipt_api()