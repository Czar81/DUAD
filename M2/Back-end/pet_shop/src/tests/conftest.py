import pytest
from src.db import (
    DbPaymentManager,
    DbUserManager,
    DbAddressManager,
    DbCartItemsManager,
    DbCartManager,
    DbProductManager,
    DbReceiptManager,
    TablesManager,
)


@pytest.fixture
def db():
    tm = TablesManager(url="sqlite:///:memory:")
    tm.create_tables()
    return tm


@pytest.fixture
def db_payment_manager(db):
    return DbPaymentManager(db)


@pytest.fixture
def db_user_manager(db):
    return DbUserManager(db)

@pytest.fixture
def db_address_manager(db):
    return DbAddressManager(db)


@pytest.fixture
def db_cart_item_manager(db):
    return DbCartItemsManager(db)

@pytest.fixture
def db_cart_manager(db):
    return DbCartManager(db)

@pytest.fixture
def db_product_manager(db):
    return DbProductManager(db)

@pytest.fixture
def db_receipt_manager(db):
    return DbReceiptManager(db)
