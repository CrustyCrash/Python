def calc(a, b, ops):
    if ops == "+":
        return a + b
    elif ops == "-":
        return a - b
    elif ops == "*":
        return a * b
    elif ops == "/":
        if b != 0:
            return round(a/b, 2)
        else:
            return ZeroDivisionError
    else:
        print("Invalid operator")


print("````Welcome to calculator````")
x = "a"
while x != "x":
    var1 = int(input("Enter variable 1 "))
    var2 = int(input("Enter variable 2 "))
    print("Operations allowed are '+' '-' '*' '/' ")
    operator = input("Enter the operation ")

    result = calc(var1, var2, operator)
    print(var1, " ", operator, " ", var2, "=", result)

    x = input("press x to exit or any other key to restart ")
print("Successfully exited")
