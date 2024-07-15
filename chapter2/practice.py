def recursive_sum(list_item):
    if len(list_item) == 0:
        return 0
    else:
        return list_item[0] + recursive_sum(list_item[1:])


print(recursive_sum([1, 2, 3, 4, 4]))
