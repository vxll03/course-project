class UserAlreadyExistsError(Exception):
    def __init__(self, username: str, message='User already exists') -> None:
        super().__init__(message)
        self.username = username


class UserDoesNotExistError(Exception):
    def __init__(self, username: str, message='User does not exists') -> None:
        super().__init__(message)
        self.username = username


class InvalidCredentialsException(Exception):
    def __init__(
        self, username: str | None = None, message='Invalid credentials'
    ) -> None:
        super().__init__(message)
        self.username = username
