# para = []
# print("Use ctrl+d to exit:")
# while True:
#     try:
#         lines = input()
#         para.append(lines)
#     except EOFError:
#         break
# with(open('user_input.txt', 'a') as file):
#     for lines in para:
#         file.write(lines + "\n")
#
#
#

print("Enter your text (use ctrl+d to exit) :")

while True:
    with (open('user_input.txt', 'a') as file):
        try:
            file.write(input() + "\n")
        except EOFError:
            break


