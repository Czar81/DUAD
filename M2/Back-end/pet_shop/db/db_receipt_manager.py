from sqlalchemy import insert, select, delete, update
from .tables_manager import TablesManager
from utils.api_exception import APIException

receipt_table = TablesManager.receipt_table
engine = TablesManager.engine


class DbReceiptManager:
    def create_receipt(self, id_cart: int, id_address: int, id_payment: int):
        stmt = (
            insert(receipt_table)
            .returning(receipt_table.c.id)
            .values(id_cart=id_cart, id_address=id_address, id_payment=id_payment)
        )

        with engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
            return result.scalar()

    def get_receipt(self, id: int | None = None, id_user: int | None = None):
        conditions = []
        if id is not None:
            conditions.append(receipt_table.c.id == id)
        if id_user is not None:
            conditions.append(receipt_table.c.id_user == id_user)

        stmt = select(receipt_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt).mappings().all()
            return result
        pass

    def update_receipt(
        self,
        id: int,
        id_cart: int,
        id_address: int,
        id_payment: int,
        state: str | None = None,
    ):
        conditions = [receipt_table.c.id == id]
        if id_user is not None:
            conditions.append(receipt_table.c.id_user == id_user) #hacer select en cart 
        stmt = update(receipt_table).where(*conditions).values(state=state)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_created = result.rowcount
            if rows_created == 0:
                raise APIException(
                    (
                        f"Receipt id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Receipt id:{str(id)} not exist"
                    ),
                    404,
                )
            else:
                conn.commit()

    def delete_cart(self, id: int, id_user: int | None = None):
        conditions = [receipt_table.c.id == id]
        if id_user is not None:
            conditions.append(receipt_table.c.id_user == id_user)
        stmt = delete(receipt_table).where(*conditions)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            rows_deleted = result.rowcount
            if rows_deleted == 0:
                raise APIException(
                    (
                        f"Receipt id:{str(id)} not exist or not owned by user id:{id_user}"
                        if id_user
                        else f"Receipt id:{str(id)} not exist"
                    ),
                    404,
                )
            conn.commit()
