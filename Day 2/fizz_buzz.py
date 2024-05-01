from fizz_buzz_func import fizz_buzz

choice = "a"
while choice != "x":
    var = int(input("Enter a value "))
    result = fizz_buzz(var)
    print(result)

    choice = input("Press x to exit or any other key to continue ")


print("Successfully exited ")
