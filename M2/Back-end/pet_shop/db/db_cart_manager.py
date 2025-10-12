from sqlalchemy import insert, select, delete, update
from .tables_manager import TablesManager
from utils.api_exception import APIException

cart_table = TablesManager.cart_table
engine = TablesManager.engine


class DbCartManager:
    def create_cart(self, id_user: int, state: str | None = None):
        values = {"id_user": id_user}
        if state is not None:
            values["state"] = state
        stmt = insert(cart_table).returning(cart_table.c.id).values(**values)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_cart(self, id: int | None = None, id_user: int | None = None):
        conditions = []
        if id is not None:
            conditions.append(cart_table.c.id == id)
        if id_user is not None:
            conditions.append(cart_table.c.id_user == id_user)

        stmt = select(cart_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            return result

    def update_cart(self, id: int, state: str, id_user: int | None = None):
        conditions = [cart_table.c.id == id]
        if id_user is not None:
            conditions.append(cart_table.c.id_user == id_user)
        stmt = update(cart_table).where(*conditions).values(state=state)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(
                    (
                        f"Cart id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Cart id:{str(id)} not exist"
                    ),
                    404,
                )
            else:
                conn.commit()

    def delete_cart(self, id: int, id_user: int | None = None):
        conditions = [cart_table.c.id == id]
        if id_user is not None:
            conditions.append(cart_table.c.id_user == id_user)
        stmt = delete(cart_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(
                    (
                        f"Cart id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Cart id:{str(id)} not exist"
                    ),
                    404,
                )
            conn.commit()
