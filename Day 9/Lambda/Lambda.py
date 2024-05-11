add = lambda a, b: a + b

print("5+10 = ", add(5, 10))

f = lambda str1: str1.upper()

print("converting hello world to upper:", f("hello world"))

f_sal = lambda sal, appraisal: round(sal * (1 + (appraisal / 100)), 2)
print("10000rs after 10% appraisal is: ", f_sal(10000,10))


height = lambda cms: round(cms * 0.0328, 2)
print("50cm = ", height(50), "ft")

conversion = lambda usd: usd * 82
print("50$ = ",conversion(50), "INR")

fare_calc = lambda price, disc: price * (100 - disc) / 100
print("100rs after 10% discount is : ", fare_calc(100, 10))
