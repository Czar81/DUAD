import jwt
import os


class JWT_Manager:
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        self.private_path = os.path.join(base_dir, "private.pem")
        self.public_path = os.path.join(base_dir, "public.pem")

    def encode(self, data):
        with open("jwt_coding/private.pem", "r") as f:
            private_key = f.read()
        encoded = jwt.encode(data, private_key, algorithm="RS256")
        return encoded

    def decode(self, token):
        with open("jwt_coding/public.pem", "r") as f:
            public_key = f.read()
        decoded = jwt.decode(token, public_key, algorithms=["RS256"])
        return decoded

