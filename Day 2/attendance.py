print("Total classes held?")
class_held = int(input())
print("Total classes attended?")
class_attended = int(input())

percent = round((class_attended/class_held)*100, 2)

print("Attendance percentage is:", percent)

if percent < 75:
    print("You are not allowed to sit for the exam")
else:
    print("You are allowed to sit for the exam")
