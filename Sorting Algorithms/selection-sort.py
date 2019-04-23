#!/usr/bin/env python3


def selection_sort(list):
    sorted_list = []
    while len(list) > 0:
        j = 0
        min_value = list[j]
        for i in range(1, len(list)):
            if list[i] < min_value:
                min_value = list[i]
                j = i
        sorted_list.append(min_value)
        del list[j]
    return sorted_list


list = [4, 1, 4, 20, 7, 2]
sorted_list = selection_sort(list)
print(sorted_list)
