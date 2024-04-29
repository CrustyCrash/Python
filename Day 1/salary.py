salary = 900
name = "John"

print (salary)
print (name)

print("raise salary by what percent?")
sal_raise = int(input())

fin_sal = salary * (1+(sal_raise/100))
print("Original Salary:", salary)
print("Salary after appraisal:", fin_sal)

