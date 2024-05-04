class NegativeNumberError(Exception):
    def __init__(self):
        print("You're too negative")


class PositiveNumberError(Exception):
    def __init__(self):
        print("You're too positive")
