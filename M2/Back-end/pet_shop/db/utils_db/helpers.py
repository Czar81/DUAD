from db.tables_manager import TablesManager

cart_table = TablesManager.cart_table


def filter_locals(locals_dict: dict, exclude: tuple = ("self",)):
    return {k: v for k, v in locals_dict.items() if k not in exclude}


def verify_user_own_cart(conn, id: int, id_user: int, table):
    stmt_select = (
        select(cart_table.c.id_user)
        .select_from(table.join(cart_table, table.c.id_cart == cart_table.c.id))
        .where(table.c.id == id)
    )

    result = conn.execute(stmt_select).fetchone()

    return True if result and result.id_user == id_user else False
