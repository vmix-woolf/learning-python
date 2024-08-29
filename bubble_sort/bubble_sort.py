import random

def bubble_sort(my_list):
    length = len(my_list)

    for lap in range(length - 1):  # lap for pairs
        swamp = False

        for j in range(length - 1 - lap):  # j for list index
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                swamp = True

        if not swamp:
            break

    return my_list


my_array = []
for i in range(1000):
    my_array.append(i)
random.shuffle(my_array)
print(my_array)
print(bubble_sort(my_array))