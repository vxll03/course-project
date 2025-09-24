class ChatDoesNotExistError(Exception):
    def __init__(self, chat_id: int, message='Chat does not exists') -> None:
        super().__init__(message)
        self.chat_id = chat_id