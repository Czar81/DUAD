class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager
    
    def _format_user(self, user_result):
        return {
            "id": user_result[0],
            "name": user_result[1],
            "email": user_result[2],
            "username": user_result[3],
            "password": user_result[4],
            "birthday": user_result[5],
        }

    def create_user(self, name, email, username, password, birthday):
        try:
            self.db_manager.execute_query(
                """INSERT INTO lyfter_car_rental."Users"(name, email, username, password, birthday, state) 
                                          VALUES(%s, %s, %s, %s, %s, 'Active')""",
                name,
                email,
                username,
                password,
                birthday,
            )
            return 201
        except Exception:
            raise

    def change_user_state(self, user_id, new_state):
        try:
            self.db_manager.execute_query(
                'UPDATE lyfter_car_rental."Users" SET state = %s WHERE id = %s',
                new_state,
                user_id,
            )
            return 200
        except Exception:
            raise
        
    def put_user_debtor(self, user_id):
        try:
            self.db_manager.execute_query(
                'UPDATE lyfter_car_rental."Users" SET state = "Debtor" WHERE id = %s',
                user_id,
            )
            return 200
        except Exception:
            raise

    def get_all_users(self):
        try:
            results = self.db_manager.execute_query('SELECT * FROM lyfter_car_rental."Users"')
            print
            formatted_results = list(map(self._format_user, results))
            return formatted_results, 200
        except Exception:
            raise
    
    def get_users_by_filters(self, **filters):
        try:
            base_query = 'SELECT * FROM lyfter_car_rental."Users"'

            where_query = [f'"{key}"=%s' for key in filters.keys()]
            params = list(filters.values())

            query = base_query + " WHERE " + " AND ".join(where_query)
            results = self.db_manager.execute_query(query, *params)

            formatted_results = list(map(self._format_user, results))
            return formatted_results, 200
        except Exception:
            raise
