import exceptions as e


def create_positive_numbered_list(my_int_list1):
    print(my_int_list1)


def create_negative_numbered_list(my_int_list2):
    print(my_int_list2)


def my_exception_store():
    my_int_list1 = []
    my_int_list2 = []
    my_het_list3 = []

    while True:
        print("Welcome to my_exception_store !!!!")
        print("-------------------------------------")
        print("Following operations are supported :")
        print("1) Create a positive numbered list  ")
        print("2) Create a negative numbered list  ")
        print("3) Refresh the program to start with blank lists")
        print("4) Exit  ")

        choice = int(input("Please enter your choice !!!! "))
        if choice == 1:
            my_int_list1 = e.Positive()
            create_positive_numbered_list(my_int_list1)

        elif choice == 2:
            my_int_list2 = e.Negative()
            create_negative_numbered_list(my_int_list2)

        elif choice == 3:
            my_int_list1.clear()
            my_int_list2.clear()
            my_het_list3.clear()
            print("Store restarted !!!! ")
        elif choice == 4:
            break
        else:
            print("Please choose something from the above")


my_exception_store()
