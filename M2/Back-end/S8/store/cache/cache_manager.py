from redis import Redis, RedisError
from dotenv import load_dotenv
from os import environ

load_dotenv()


class CacheManager:
    def __init__(
        self,
    ):
        self.host = environ.get("REDIS_HOST")
        self.port = int(environ.get("REDIS_PORT"))
        self.password = environ.get("REDIS_KEY")
        self.redis_client = Redis(
            host=self.host, port=self.port, password=self.password
        )

    def store_data(self, key: str, values: str, time_to_live: int = None):
        try:
            if time_to_live is None:
                self.redis_client.hset(key, mapping=values)
            else:
                self.redis_client.hsetex(key, mapping=values, ex=time_to_live)
        except RedisError as error:
            print(f"An error ocurred while storing data in Redis: {error}")

    def check_key(self, key: str):
        try:
            key_exists = self.redis_client.exists(key)
            if key_exists:
                ttl = self.redis_client.ttl(key)
                return True, ttl

            return False, None
        except RedisError as error:
            print(f"An error ocurred while checking a key in Redis: {error}")
            return False, None

    def get_data(self, key: str):
        try:
            output = self.redis_client.hgetall(key)

            if output is not None:
                result = {k.decode(): v.decode() for k, v in output.items()}
                return result
            else:
                return None
        except RedisError as e:
            print(f"An error ocurred while retrieving data from Redis: {e}")

    def delete_data(self, key: str):
        try:
            output = self.redis_client.delete(key)
            if output > 0:
                print(f"Key '{key}' and its value have been deleted.")
            else:
                print(f"Key '{key}' not found.")

            return output == 1
        except RedisError as e:
            print(f"An error ocurred while deleting data from Redis: {e}")
            return False

    def delete_data_with_pattern(self, pattern):
        try:
            for key in self.redis_client.scan_iter(match=pattern):
                self.redis_client.delete(key)
        except RedisError as error:
            print(f"An error ocurred while deleting data from Redis: {error}")
