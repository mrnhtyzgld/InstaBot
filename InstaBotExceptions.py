class InstaBotException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.args[0]}"

class TimeOut(InstaBotException):
    def __init__(self, message):
        super().__init__(message)
