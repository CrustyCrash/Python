print("enter marks")
marks = int(input())

if marks > 80:
    print("A")
elif 60 < marks < 80:
    print("B")
elif 50 < marks < 60:
    print("C")
elif 40 < marks < 50:
    print("D")
elif 25 <= marks < 40:
    print("E")
else:
    print("F")
