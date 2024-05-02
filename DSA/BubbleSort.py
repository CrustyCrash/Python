import dict


def bubbleSort(cards):

    for i in range(len(cards)):
        for j in range(0, len(cards)-i-1):
            if cards[j] > cards[j + 1]:
                (cards[j], cards[j + 1]) = (cards[j + 1], cards[j])

    print(cards)


bubbleSort(dict.my_dict['input']['cards'])
