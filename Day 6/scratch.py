class My_exception(Exception):
    def __init__(self):
        print("I was executed")

    def func(self):
        print("Hello")


obj = My_exception()


def func():
    print("Hello")

try:
    raise My_exception().func()
except:
    pass


