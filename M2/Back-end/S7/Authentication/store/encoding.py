import jwt


class JWT_Manager:
    def __init__(self, secret="HelloThere", algorithm="HS256"):
        self.secret = secret
        self.algorithm = algorithm

    @classmethod
    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.secret, algorithm=self.algorithm)
            return encoded
        except:
            return None

    @classmethod
    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None
