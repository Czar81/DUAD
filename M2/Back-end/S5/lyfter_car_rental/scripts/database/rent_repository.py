class RentRepository:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_rent(self, fk_car_id, fk_user_id, rent_date, state):
        try:
            self.db_manager.execute_query(
                """INSERT INTO "Rents" (fk_car_id, fk_user_id, rent_date, state)
                                          VALUES(%s,%s,%s,%s);""",
                fk_car_id,
                fk_user_id,
                rent_date,
                state,
            )
            print("User create successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def car_returned(self, rent_id):
        try:
            self.db_manager.execute_query(
                """
                UPDATE "Rents" SET state = 'Return' WHERE id = %s; 
                UPDATE "Cars" SET state = 'Available' WHERE id = (SELECT fk_car_id FROM "Rents" WHERE id = %s);
                """,
                rent_id,
                rent_id,
            )
        except Exception as e:
            print(f"Error: {e}")
