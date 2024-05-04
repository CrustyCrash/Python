def set_union(setA, setB):
    print(setA.union(setB))


def set_intersection(setA, setB):
    print(setA.intersection(setB))


def set_minus(setA, setB):
    print(setA.difference(setB))


def set_minusB(setB, setA):
    print(setB.difference(setA))


def is_member_of_set(setB):
    element = input("Enter element ")
    if element in setB:
        print("True")
    else:
        print("False")


def set_display(setA):
    print(len(setA))


def set_displayB(setB):
    print(len(setB))


def set_add_element(setA):
    setA.add(input("Enter element: "))


def set_add_elements(setA):
    setA.update(input("Enter elements separated by comma: ").split(","))


def set_remove_element(setA):
    setA.remove(input("Enter element name to remove: "))


def my_set_store():
    print("\n Welcome to Our Set Store !!! ")

    setA = set()
    listA = []
    listA.append(int(input("Enter int separated by comma ")))
    for i in listA:
        el

    setB = set(input("Please enter comma seperated elements for the set B").split(","))

    while (True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("	1: Union")
        print("	2: Intersection ")
        print("	3: A-B")
        print("	4: B-A")
        print("	5: Take a element from user and Display if that element is a member of set B ")
        print("	6: Display number of elements in the set A")
        print(" 7: Display number of elements in the set B")
        print("	8: Add an element taken from the user to the set A")
        print("	9: Add multiple elements taken from the user to the set A")
        print("	10: Remove an element taken from the user from set A")
        print(" 11: Exit")

        choice = int(input("Please enter your choice "))

        if choice == 1:
            set_union(setA, setB)
        elif choice == 2:
            set_intersection(setA, setB)
        elif choice == 3:
            set_minus(setA, setB)
        elif choice == 4:
            set_minus(setB, setA)
        elif choice == 5:
            is_member_of_set(setB)
        elif choice == 6:
            set_display(setA)
        elif choice == 7:
            set_display(setB)
        elif choice == 8:
            set_add_element(setA)
        elif choice == 9:
            set_add_elements(setA)
        elif choice == 10:
            set_remove_element(setA)
        elif choice == 11:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")


my_set_store()
