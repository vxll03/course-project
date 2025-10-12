class ChatDoesNotExistError(Exception):
    def __init__(self, chat_name: str, message='Chat does not exists') -> None:
        super().__init__(message)
        self.chat_name = chat_name