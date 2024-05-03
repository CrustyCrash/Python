def dict_display_capitals(capitals):
    print(capitals)


def dict_add_element(capitals):
    print("Enter key:value")
    keys, values = input().split(":")
    capitals.update({keys: values})


def dict_add_elements(capitals):
    key_val = input("Enter keys:values ")
    table = key_val.maketrans(",", ":")
    key_val = key_val.translate(table)
    new_str = key_val.split(":")
    keys = new_str[::2]
    values = new_str[1::2]

    for i in range(0, len(keys)):
        capitals[keys[i]] = values[i]


def dict_remove_element(capitals):
    capitals.pop(input("Enter the key "))


def dict_show_value_for_a_key(capitals):
    print(capitals.get(input("Enter key: ")))


def dict_update_or_add_a_key(capitals):
    capitals.update({input("Enter key "): input("Enter value")})


def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")

    capitals = {}
    """
        # Write your code here to create the dictionary from the user and reference it with capitals
    """

    keys = input("Please enter the countries as keys for ex : India,USA,Srilanka ").split(',')
    for elem in keys:
        capitals[elem] = input(f"Please enter the capital for {elem}: ").strip()
    print(capitals)

    while True:
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display all elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print(
            '3: Add multiple elements to the capitals collection like -->  Albania:Tirane,Algeria:Algiers,'
            'Andorra:Andorra la Villa')
        print("    4: Remove an element from the collection 	")
        print("    5: Show value for a key 	")
        print("    6: Update or add capital 	")
        print("    7: Exit the Program ")
        choice = int(input("Please enter your choice "))

        if choice == 1:
            dict_display_capitals(capitals)
        elif choice == 2:
            dict_add_element(capitals)
        elif choice == 3:
            dict_add_elements(capitals)
        elif choice == 4:
            dict_remove_element(capitals)
        elif choice == 5:
            dict_show_value_for_a_key(capitals)
        elif choice == 6:
            dict_update_or_add_a_key(capitals)
        elif choice == 7:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")


my_dict_store()
