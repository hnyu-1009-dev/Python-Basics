print("common_exceptions.py被引用了")


class CustomException(Exception):
    def __init__(self, message, error_code=None, traceback=None):
        super().__init__(message)
        self.error_code = error_code
        self.traceback = traceback


raise CustomException("Something went wrong", 123, "Traceback")
