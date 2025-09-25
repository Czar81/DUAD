import jwt


class JWT_Manager:

    def __init__(
        self,
        public_key="8b1a9953c4611296a827abf8c47804d7",
        private_key="b37668c1bcfa28cf8fc3fbe07ecee536",
    ):
        self.public_key = public_key
        self.private_key = private_key
        self.algorithm = "RS256"

    @classmethod
    def encode(self, data):
        encoded = jwt.encode(data, self.private_key, algorithm=self.algorithm)
        return encoded

    def decode(self, token):
        decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
        return decoded
