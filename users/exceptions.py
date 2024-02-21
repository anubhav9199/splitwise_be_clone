class UserNotFoundException(Exception):
    """Raised when user not found."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
