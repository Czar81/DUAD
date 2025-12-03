from jwt import encode, decode
from os import environ
from dotenv import load_dotenv

load_dotenv()


class JWT_Manager:
    def __init__(self):
        self.private_key = environ.get("PRIVATE_KEY")
        self.public_key = environ.get("PUBLIC_KEY")
        if not self.private_key or not self.public_key:
            raise ValueError("PRIVATE_KEY y PUBLIC_KEY must be defiend in .env")
    def encode(self, data):
        try:
            encoded = encode(data, self.private_key, algorithm="RS256")
            return encoded
        except Exception as e:
            raise ValueError(f"Error encoding JWT: {str(e)}")
    def decode(self, token):
        try:
            decoded = decode(token, self.public_key, algorithms=["RS256"])
            return decoded
        except Exception as e:
            raise ValueError(f"Error decoding JWT: {str(e)}")
