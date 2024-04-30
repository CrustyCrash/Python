def div(val):
    if val % 3 == 0 and val % 5 == 0:
        print("Fizz Buzz")
    elif val % 5 == 0:
        print("Buzz")
    elif val % 3 == 0:
        print("Fizz")
    else:
        print("Invalid Input")
