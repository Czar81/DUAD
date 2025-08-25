class DbManager:
    def __init__(self, engine, select, insert, update, delete):
        self.engine = engine
        self.select = select
        self.insert = insert
        self.update = update
        self.delete = delete

    def insert_table(self, user_table, name):
        stmt = self.insert(user_table).values(name=name)
        with self.engine.connect() as connection:
            result = connection.execute(stmt)  # What this return?
            connection.commit()

    def update_table(self, user_table, id, name):
        stmt = self.update(user_table).where(user_table.c.id == id).values(name=name)
        with self.engine.connect() as connection:
            result = connection.execute(stmt)
            connection.commit()

    def delete_table(self, user_table, id):
        stmt = self.delete(user_table).where(user_table.c.id == id)
        with self.engine.connect() as connection:
            result = connection.execute(stmt)
            connection.commit()
