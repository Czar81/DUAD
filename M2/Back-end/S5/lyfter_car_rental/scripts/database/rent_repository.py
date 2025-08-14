class RentRepository:

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rent(self, rent_result):
        return {
            "id": rent_result[0],
            "fk_car_id": rent_result[1],
            "fk_user_id": rent_result[2],
            "rent_date": rent_result[3],
            "state": rent_result[4],
        }

    def create(self, request_body):
        try:
            state = self.db_manager.execute_query(
                'SELECT state FROM lyfter_car_rental."Cars" WHERE id = %s',
                request_body["fk_car_id"],
            )
            if state != "Available":
                raise ValueError("Car unavailable")
            self.db_manager.execute_query(
                """
                INSERT INTO lyfter_car_rental."Rents" (fk_car_id, fk_user_id, state)
                VALUES(%s,%s,'Active');
                """,
                request_body["fk_car_id"],
                request_body["fk_user_id"],
            )
            self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental."Cars" 
                SET state = 'Rented'
                WHERE id = %s
                """,
                request_body["fk_car_id"],
            )
            return 201
        except Exception:
            raise

    def car_returned(self, rent_id):
        try:
            self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental."Rents" 
                SET state = 'Return' 
                WHERE id = %s; 
                """,
                rent_id,
            )
            self.db_manager.execute_query(
                """
                UPDATE lyfter_car_rental."Cars" 
                SET state = 'Available' 
                WHERE id = (SELECT fk_car_id FROM lyfter_car_rental."Rents" WHERE id = %s); 
                """,
                rent_id,
            )
        except Exception:
            raise

    def change_state(self, rent_id, new_state):
        try:
            self.db_manager.execute_query(
                'UPDATE lyfter_car_rental."Rents" SET state = %s WHERE id = %s',
                new_state,
                rent_id,
            )
            return 200
        except Exception:
            raise

    def get_all(self):
        try:
            results = self.db_manager.execute_query(
                'SELECT * FROM lyfter_car_rental."Rents"'
            )
            formatted_results = list(map(self._format_rent, results))
            return formatted_results, 200
        except Exception:
            raise

    def get_by_filters(self, **filters):
        try:
            base_query = 'SELECT * FROM lyfter_car_rental."Rents"'

            where_query = [f'"{key}"=%s' for key in filters.keys()]
            params = list(filters.values())

            query = base_query + " WHERE " + " AND ".join(where_query)
            results = self.db_manager.execute_query(query, *params)

            formatted_results = list(map(self._format_rent, results))
            return formatted_results, 200
        except Exception:
            raise
