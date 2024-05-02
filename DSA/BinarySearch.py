import dict


def binary_search(cards, query, start, end):

    while start <= end:
        mid = int(start + (end - start) / 2)
        # print(mid)
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            start = mid + 1
        elif cards[mid] > query:
            end = mid - 1
    return -1


dict.my_dict['input']['cards'].sort()
print(binary_search(dict.my_dict['input']['cards'], dict.my_dict['query'], 0, len(dict.my_dict['input']['cards'])-1))
