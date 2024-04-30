def add(var1, var2):
    print(var1, " + ", var2, " = ", var1 + var2)
    print("Square of ", var1, "is:", var1 * var1)
    print(var1, "^", var2, " = ", (var1 ** var2))


print("Enter first num :")
first_var = int(input())
print("Enter second num :")
sec_var = int(input())

add(first_var, sec_var)


def upper(var3):
    return var3.upper()


print("Your input:")
str_var = input()

print("Original string: ", str_var)
print("Modified string: ", upper(str_var))


def sal_calc(sal, appraisal):
    return round(sal * (1 + (appraisal / 100)), 2)


salary = 900
name = "John"

print(salary)
print(name)

print("raise salary by what percent?")
sal_raise = int(input())

print("Original Salary:", salary)
print("Salary after appraisal:", sal_calc(salary, sal_raise))


def height(cms):
    return round(cms * 0.0328, 2)


print("Enter height in cms")
cm_height = int(input())
print("Converted height: ", height(cm_height), "Foot")


def conversion(usd):
    return usd * 82


print("Enter amount in $")
dollar = int(input())
print(dollar, "$ = ", conversion(dollar), "Rs.")


def fare_calc(price, disc):
    return price * (100 - disc) / 100


print("Enter source")
source = input()
print("Enter destination")
destination = input()
print("Enter fare")
fare = int(input())
print("Enter discount")
discount = int(input())

print("Fare from", source, "to", destination, "is", fare, "INR,", "after applied discount of", discount, "% it is ",
      fare_calc(fare, discount), "INR")
