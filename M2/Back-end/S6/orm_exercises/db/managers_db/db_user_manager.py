class DbUserManager:
    def __init__(self, engine, select, insert, update, delete):
        self.engine = engine
        self.select = select
        self.insert = insert
        self.update = update
        self.delete = delete

    def insert_user(self, user_table, name):
        stmt = self.insert(user_table).values(name=name)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return f"Inserted {str(result.inserted_primary_key[0])} row successfully"

    def update_user(self, user_table, id, name):
        stmt = self.update(user_table).where(user_table.c.id == id).values(name=name)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return result.rowcount

    def delete_user(self, user_table, id):
        stmt = self.delete(user_table).where(user_table.c.id == id)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return result.rowcount
