class UserException(Exception):
    def __init__(self, code, message):
        super(UserException, self).__init__(message)
        self.code = code
        self.message = message


class AuthException(Exception):
    def __init__(self, message):
        super(AuthException, self).__init__(message)
        self.message = message


class OtherException(Exception):
    def __init__(self, message):
        super(OtherException, self).__init__(message)
        self.message = message
