def AgeException():
    print("you lived for so long , may be you will die soon:)")


def age():
    try:
        if int(input("Enter age ")) * 365 < 10000:
            print("You're too young, Do you know da wae my brudda?")
        else:
            raise AgeException()
    finally:
        print("Exiting gracefully")
        exit()


age()
