import dict


def selectionSort(cards):

    for i in range(len(cards)):
        minimum = i
        for j in range(i+1, len(cards)):
            if cards[j] < cards[minimum]:
                minimum = j
        (cards[i], cards[minimum]) = (cards[minimum], cards[i])

    print(cards)


selectionSort(dict.my_dict['input']['cards'])