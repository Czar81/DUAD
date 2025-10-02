from jwt import encode, decode
from os import environ
from dotenv import load_dotenv
load_dotenv()

class JWT_Manager:
    def __init__(self):
        self.private_key = os.environ.get("PRIVATE_KEY")
        self.public_key = os.environ.get("PUBLIC_KEY")

    def encode(self, data):
        encoded = jwt.encode(data, self.private_key, algorithm="RS256")
        return encoded

    def decode(self, token):
        decoded = jwt.decode(token, self.public_key, algorithms=["RS256"])
        return decoded

