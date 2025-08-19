import psycopg2

class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = self.__create_connection(db_name, user, password, host, port)
        if self.connection:
            self.cursor = self.connection.cursor()

    def __create_connection(self, db_name, user, password, host, port):
        try:
            connection = psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port,
            )
            return connection
        except Exception:
            raise

    def execute_query(self, query, *args):
        try:
            self.cursor.execute(query, args)
            self.connection.commit()

            if self.cursor.description:
                results = self.cursor.fetchall()
                return results
        except Exception:
            raise

    def close_connection(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            return "Connection closed", 200
        except Exception:
            raise