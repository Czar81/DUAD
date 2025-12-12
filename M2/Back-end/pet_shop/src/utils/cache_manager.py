from redis import Redis, RedisError
from .api_exception import APIException
from dotenv import load_dotenv
from json import dumps, loads
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

    def store_data(self, key: str, values: list, time_to_live: int = None):
        try:
            list_str = dumps(values)
            if time_to_live is None:
                self.redis_client.set(key, list_str)
            else:
                self.redis_client.setex(key, time_to_live, list_str)
        except RedisError as error:
            raise RedisError(f"An error ocurred while storing data in Redis: {error}")

    def check_key(self, key: str):
        try:
            key_exists = self.redis_client.exists(key)
            if key_exists:
                return True
            return False
        except RedisError as error:
            raise RedisError(f"An error ocurred while checking a key in Redis: {error}")

    def get_data(self, key: str):
        try:
            output = self.redis_client.get(key)

            if output is not None:
                if isinstance(output, bytes):
                    output = output.decode("utf-8")
                result = loads(output)
                return result
            else:
                return None
        except RedisError as e:
            raise RedisError(f"An error ocurred while retrieving data from Redis: {e}")

    def delete_data(self, key: str):
        try:
            output = self.redis_client.delete(key)

        except RedisError as e:
            raise RedisError(f"An error ocurred while deleting data from Redis: {e}")

    def delete_data_with_pattern(self, pattern):
        try:
            for key in self.redis_client.scan_iter(match=pattern):
                self.redis_client.delete(key)
        except RedisError as error:
            raise RedisError(
                f"An error ocurred while deleting data from Redis: {error}"
            )
