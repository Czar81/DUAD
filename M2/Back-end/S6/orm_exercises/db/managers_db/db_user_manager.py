class DbUserManager:
    def __init__(self, user_table, engine, select, insert, update, delete):
        self.user_table = user_table
        self.engine = engine
        self.select = select
        self.insert = insert
        self.update = update
        self.delete = delete
    
    def get_all_user(self):
        stmt = self.select(self.user_table)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return result.all()

    def create_user(self, name):
        stmt = self.insert(self.user_table).values(name=name)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return (f"Create user id:{result.inserted_primary_key[0]} successfully")

    def update_user(self, id, name):
        stmt = self.update(self.user_table).where(self.user_table.c.id == id).values(name=name)
        with self.engine.begin() as connection:
            connection.execute(stmt)

    def delete_user(self, id):
        stmt = self.delete(self.user_table).where(self.user_table.c.id == id)
        with self.engine.begin() as connection:
            connection.execute(stmt)
