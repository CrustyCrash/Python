import dict


def linear_search(cards, query):
    position = 0

    while True:
        if cards[position] == query:
            return position

        position += 1

        if position == len(cards):
            print("Element not found ")
            return -1


print(linear_search(dict.my_dict['input']['cards'], dict.my_dict['query']))
