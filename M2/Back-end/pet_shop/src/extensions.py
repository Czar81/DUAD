from src.utils import JWT_Manager, CacheManager
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

db_payment_manager = DbPaymentManager(TablesManager)
db_user_manager = DbUserManager(TablesManager)
db_address_manager =DbAddressManager(TablesManager)
db_cart_manager = DbCartManager(TablesManager)
db_cart_item_manager = DbCartItemsManager(TablesManager)
db_product_manager=DbProductManager(TablesManager),
db_receipt_manager=DbReceiptManager(TablesManager)
cache_manager = CacheManager()
jwt_manager = JWT_Manager()
