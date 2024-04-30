def add(var1, var2):
    print(var1, " + ", var2, " = ", var1 + var2)
    print("Square of ", var1, "is:", var1 * var1)
    print(var1, "^", var2, " = ", (var1 ** var2))


def upper(var3):
    return var3.upper()


def sal_calc(sal, appraisal):
    return round(sal * (1 + (appraisal / 100)), 2)


def height(cms):
    return round(cms * 0.0328, 2)


def conversion(usd):
    return usd * 82


def fare_calc(price, disc):
    return price * (100 - disc) / 100

