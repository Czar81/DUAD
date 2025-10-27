from .tables_manager import TablesManager
from sqlalchemy import select, and_

def _filter_locals(table, locals_dict: dict, exclude: tuple = ("self",)):
    filtered={k: v for k, v in locals_dict.items() if k not in exclude and v is not None}
    return [getattr(table.c, k)== v for k, v in filtered.items()]


def _filter_values(locals_dict: dict, exclude:tuple=("self",)):
    return {k:v for k, v in locals_dict.items() if k not in exclude and v is not None}


def _verify_user_own_cart(conn, id_user: int, id_table:int | None = None,id_cart:int | None = None, table=None):
    cart_table = TablesManager.cart_table
    if id_user is None:
        return False
    if id_table is not None and table is not None:
        stmt = (select(cart_table.c.id_user).select_from(table.join(cart_table, table.c.id_cart == cart_table.c.id)).where(table.c.id == id_table))
    else: 
        stmt= select(cart_table.c.id_user).where(and_(cart_table.c.id_user==id_user, cart_table.c.id==id_cart))
    result = conn.execute(stmt).fetchone()
    return bool(result and result.id_user == id_user)
