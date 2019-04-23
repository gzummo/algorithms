#!/usr/bin/env python3


def insertion_sort(list):
    for i in range(1, len(list)):
        current_item = list[i]
        j = i - 1
        while j >= 0 and list[j] > current_item:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = current_item
    return list


list = [4, 1, 4, 20, 7, 2]
insertion_sort(list)
print(list)
