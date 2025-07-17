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
                birthday
            )
            print("User create successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def chage_user_state(self, user_id, new_state):
        try:
            self.db_manager.execute_query(
                'UPDATE lyfter_car_rental."Users" SET state = %s WHERE id = %s',
                new_state,
                user_id,
            )
        except Exception as e:
            print(f"Error: {e}")
