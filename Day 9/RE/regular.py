import re

string1 = 'gaurav1234@gmail.com'
string2 = 'pratik190900234@gmail.com'
string3 = '2009_rocking_person@yahoo.com'
string4 = 'GodFather2022@yahoo.com'
string5 = 'Brocklesner_89_WWE@yahoo.com'
string6 = 'TheRock_WWE@yahoo.com'
string7 = 'JohnCena_WWE@yahoo.com'
string8 = 'Undertaker_Roman_reigns@outlook.com'
string9 = '6789764666@rediffmail.com'
string10 = 'Kane#6789@gmail.com'
string11 = '2009ROCKING_PERSON@yahoo.com'

my_list = [string1, string2, string3, string4, string5, string6, string7, string8, string9, string10, string11]

# 1) provide me the list of emails that do have special characters of #~`!


pattern = r"[\#|\~|\`|\!]"

for test_string in my_list:
    result = re.search(pattern, test_string)
    if result:
        print(test_string)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# provide me the list of emails that start with numbers
pattern2 = r"^[\d]."

for test_string in my_list:
    result = re.search(pattern2, test_string)
    if result:
        print(test_string)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# # 3) provide me the list of emails that start with numbers followed by an underscore

patter3 = r'^\d+_\w+'

for test in my_list:
    result = re.search(patter3,test)
    if result:
        print(test)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# # 4) provide me the list of emails that start with numbers followed by an underscore or small case characters

pattern4 = r'^\d+(_|a-z)'
for pat4 in my_list:
    result = re.search(pattern4, pat4)
    if result:
        print(pat4)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# # 5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters

pattern4 = r'^[0-9]+[_a-zA-Z]'
for pat4 in my_list:
    result = re.search(pattern4, pat4)
    if result:
        print(pat4)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# # 6) Provide me list of emails with only numbers before the @

pattern4 = r'^\d+@'
for pat4 in my_list:
    result = re.search(pattern4, pat4)
    if result:
        print(pat4)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# # 7) Provide me list of emails with numbers anywhere before the @
pattern4 = r'\d'
for pat4 in my_list:
    result = re.search(pattern4, pat4)
    if result:
        print(pat4)

