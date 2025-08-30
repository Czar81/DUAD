class DbAddressManager:
    def __init__(self, address_table, engine, select, insert, update, delete):
        self.address_table = address_table
        self.engine = engine
        self.select = select
        self.insert = insert
        self.update = update
        self.delete = delete
    
    def get_all_address(self):
        stmt = self.select(self.address_table)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return result.all()

    def create_address(self, address:str, user_id:int):
        stmt = self.insert(self.address_table).values(address=address, user_id=user_id)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return (f"Create address id:{result.inserted_primary_key[0]} successfully")

    def update_address(self, id:int, address:str, user_id:int):
        stmt = self.update(self.address_table).where(self.address_table.c.id == id).values(address=address, user_id=user_id)
        with self.engine.begin() as connection:
            connection.execute(stmt)

    def delete_address(self, id:int):
        stmt = self.delete(self.address_table).where(self.address_table.c.id == id)
        with self.engine.begin() as connection:
            connection.execute(stmt)
