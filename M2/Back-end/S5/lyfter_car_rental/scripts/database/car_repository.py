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
            return 201
            # add to API print("Car add successfully!")
        except Exception:
            raise

    def change_car_state(self, car_id, new_state):
        try:
            self.db_manager.execute_query(
                """UPDATE lyfter_car_rental."Cars" 
                                        SET state = %s 
                                        WHERE id = %s""",
                new_state,
                car_id,
            )
            return 200
        except Exception:
            raise

    def get_all_cars(self):
        try:
            results = self.db_manager.execute_query('SELECT * FROM lyfter_car_rental."Cars"')
            formatted_results = list(map(self._format_car, results))
            return formatted_results, 200
        except Exception:
            raise
    
    def get_cars_by_filters(self, **filters):
        try:
            base_query = 'SELECT * FROM lyfter_car_rental."Cars"'

            where_query = [f'"{key}"=%s' for key in filters.keys()]
            params = list(filters.values())

            query = base_query + " WHERE " + " AND ".join(where_query)
            results = self.db_manager.execute_query(query, *params)

            formatted_results = list(map(self._format_car, results))
            return formatted_results, 200
        except Exception:
            raise