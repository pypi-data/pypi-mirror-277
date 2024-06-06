import jwt


class JWTAuthorize:
    verifyOption = {
        'verify_signature': False
    }

    def __init__(self, algorithm='HS512'):
        self.secret = "abcdefghijklmnopqrstuvwxyz"
        self.algorithm = algorithm

    def decode(self, token):
        return jwt.decode(token, self.secret, algorithms=self.algorithm, options=self.verifyOption)

    def encode(self, payload):
        return jwt.encode(payload=payload, key=self.secret, algorithm=self.algorithm)
