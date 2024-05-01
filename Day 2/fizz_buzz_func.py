def fizz_buzz(num):
    if num % 5 == 0:
        if num % 3 == 0:
            return "Fizz Buzz"
        else:
            return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return "Invalid Input"
