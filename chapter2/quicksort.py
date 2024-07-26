import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = random.choice(arr)
    less = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
