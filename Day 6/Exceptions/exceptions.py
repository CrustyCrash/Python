import ExceptionClass as Ec


def Positive():
    my_int_list1 = []
    try:
        while True:
            try:
                user_input = int(input("Enter positive numbers (enter any character to exit)"))
                if user_input < 0:
                    raise Ec.NegativeNumberError
                my_int_list1.append(user_input)
            except ValueError:
                break
        return my_int_list1

    except Ec.NegativeNumberError:
        print("We received a negative number in the list and I handled negative number error exception")
        my_int_list1.clear()
        exit()


def Negative():
    my_int_list2 = []
    try:
        while True:
            try:
                user_input = int(input("Enter negative numbers (enter any character to exit) "))
                if user_input > 0:
                    raise Ec.PositiveNumberError
                my_int_list2.append(user_input)
            except ValueError:
                break
        return my_int_list2

    except Ec.PositiveNumberError:

        print("We received a positive number in the list and I handled positive_number_error exception")
        my_int_list2.clear()
        exit()
