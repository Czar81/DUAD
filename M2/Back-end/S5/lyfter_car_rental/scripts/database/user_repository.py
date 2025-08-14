class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

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

    def get_all_users(self):
        try:
            results = self.db_manager.execute_query('SELECT * FROM lyfter_car_rental."Users"')
            return results, 200
        except Exception:
            raise
    
    def get_users_by_filters(self, **filter):
        try:
            base_query = 'SELECT * FROM lyfter_car_rental."Users"'

            where_query = [f'"{key}"=%s' for key in filter.keys()]
            params = list(filter.values())

            query = base_query + " WHERE " + " AND ".join(where_query)
            results = self.db_manager.execute_query(query, *params)

            return results, 200
        except Exception:
            raise
