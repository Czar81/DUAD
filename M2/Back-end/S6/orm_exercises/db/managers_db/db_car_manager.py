class DbCarManager:
    def __init__(self, car_table, engine, select, insert, update, delete):
        self.car_table = car_table
        self.engine = engine
        self.select = select
        self.insert = insert
        self.update = update
        self.delete = delete
    
    def get_all_cars(self):
        stmt = self.select(self.car_table)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return result.all()

    def create_car(self, model:str, user_id:int):
        stmt = self.insert(self.car_table).values(model=model, user_id=user_id)
        with self.engine.begin() as connection:
            result = connection.execute(stmt)
            return (f"Create car id:{result.inserted_primary_key[0]} successfully")

    def update_car(self, id:int, model:str, user_id:int):
        stmt = self.update(self.car_table).where(self.car_table.c.id == id).values(model=model, user_id=user_id)
        with self.engine.begin() as connection:
            connection.execute(stmt)

    def update_user_for_car(self, id:int, user_id:int):
        stmt = self.update(self.car_table).where(self.car_table.c.id == id).values(user_id=user_id)
        with self.engine.begin() as connection:
            connection.execute(stmt)

    def delete_car(self, id:int):
        stmt = self.delete(self.car_table).where(self.car_table.c.id == id)
        with self.engine.begin() as connection:
            connection.execute(stmt)
