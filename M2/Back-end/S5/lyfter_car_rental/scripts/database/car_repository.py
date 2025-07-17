class CarRepository:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self, car_result):
        return {
            "id": car_result[0],
            "make": car_result[1],
            "model": car_result[2],
            "year": car_result[3],
            "state": car_result[4],
        }

    def create_car(self, make, model, year, state):
        try:
            self.db_manager.execute_query(
                """INSERT INTO lyfter_car_rental."Cars"(make, model, year, state) 
                                        VALUES(%s,%s,%s,%s)""",
                make,
                model,
                year,
                state,
            )
            print("Car add successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def chage_car_state(self, car_id, new_state):
        try:
            self.db_manager.execute_query(
                """UPDATE lyfter_car_rental."Cars" 
                                        SET state = %s 
                                        WHERE id = %s""",
                new_state,
                car_id,
            )
        except Exception as e:
            print(f"Error: {e}")

    def disable_car(self, car_id):
        try:
            self.db_manager.execute_query(
                """UPDATE lyfter_car_rental."Cars" 
                                        SET state = 'Unavailable' 
                                        WHERE id = %s""",
                car_id,
            )
        except Exception as e:
            print(f"Error: {e}")

    def get_rented(self):
        try:
            results = self.db_manager.execute_query(
                """SELECT * FROM lyfter_car_rental."Cars" WHERE state = 'Rented'"""
            )
            formatted_results = list(map(self._format_car, results))
            return formatted_results
        except Exception as e:
            print(f"Error: {e}")

    def get_available(self):
        try:
            results = self.db_manager.execute_query(
                """SELECT * FROM lyfter_car_rental."Cars" WHERE state = 'Available'"""
            )
            formatted_results = list(map(self._format_car, results))
            return formatted_results
        except Exception as e:
            print(f"Error: {e}")

    def get_all():
        pass
