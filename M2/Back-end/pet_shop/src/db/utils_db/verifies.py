from .tables_manager import TablesManager
from sqlalchemy import select, and_

payment_table = TablesManager.payment_table
address_table = TablesManager.address_table
product_table = TablesManager.product_table
cart_table = TablesManager.cart_table


def _verify_amount_product(conn, id_product, amount_bought):
    stmt = select(product_table.c.amount).where(product_table.c.id == id_product)
    result = conn.execute(stmt).fetchone()
    if result is None:
        raise ValueError(f"Product with id {id_product} not found")
    
    actual_amount = result[0]
    
    if actual_amount < amount_bought:
        raise ValueError(
            f"Insufficient stock. Available: {actual_amount}, Requested: {amount_bought}"
        )
    if actual_amount is None:
        return False
    new_amount = actual_amount - amount_bought
    return new_amount, actual_amount


def _verify_user_own_cart(
    conn,
    id_user: int | None = None,
    id_table: int | None = None,
    id_cart: int | None = None,
    table=None,
):
    if id_user is None:
        return True
    if id_table is not None and table is not None:
        stmt = (
            select(cart_table.c.id_user)
            .select_from(table.join(cart_table, table.c.id_cart == cart_table.c.id))
            .where(table.c.id == id_table)
        )
    else:
        stmt = select(cart_table.c.id_user).where(
            and_(cart_table.c.id_user == id_user, cart_table.c.id == id_cart)
        )
    result = conn.execute(stmt).fetchone()
    return bool(result and result.id_user == id_user)


def _verify_user_own_payment(conn, id_payment: int, id_user: int | None = None):
    if id_user is None:
        return True
    stmt = select(payment_table.c.id_user).where(
        and_(payment_table.c.id == id_payment, payment_table.c.id_user == id_user)
    )
    result = conn.execute(stmt).fetchone()
    return bool(result and result.id_user == id_user)


def _verify_user_own_address(conn, id_address: int, id_user: int | None = None):
    if id_user is None:
        return True
    stmt = select(address_table.c.id_user).where(
        and_(address_table.c.id == id_address, address_table.c.id_user == id_user)
    )
    result = conn.execute(stmt).fetchone()
    return bool(result and result.id_user == id_user)
