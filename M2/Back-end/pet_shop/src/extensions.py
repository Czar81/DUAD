from src.utils.encoding import JWT_Manager
from src.utils.cache_manager import CacheManager
from src.db import (
    DbPaymentManager,
    DbUserManager,
    DbAddressManager,
    DbCartItemsManager,
    DbCartManager,
    DbProductManager,
    DbReceiptManager,
    TablesManager
)
tm = TablesManager()
db_payment_manager = DbPaymentManager(tm)
db_user_manager = DbUserManager(tm)
db_address_manager =DbAddressManager(tm)
db_cart_manager = DbCartManager(tm)
db_cart_item_manager = DbCartItemsManager(tm)
db_product_manager=DbProductManager(tm)
db_receipt_manager=DbReceiptManager(tm)
cache_manager = CacheManager()
jwt_manager = JWT_Manager()
