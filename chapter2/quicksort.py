import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = random.choice(arr)
        less = [i for i in arr if i > pivot]
        greater = [i for i in arr if i < pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 2, 4, 1, 9, 0]))
