fruits = ["apple", "orange", "banana", "mango", "pineapple"]

try:
    print(fruits[int(input("Enter index number "))])

except IndexError:
    print("Index out of bound")
    exit()
