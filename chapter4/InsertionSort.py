#Implement an insertion sort algorithm

def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        num_to_order = my_list[i]
        j = i - 1
        # Shift elements of the sorted part of the list to the right
        while j >= 0 and my_list[j] > num_to_order:
            my_list[j + 1] = my_list[j]
            j -= 1
        # Place the current number in its correct position
        my_list[j + 1] = num_to_order
    return my_list

my_list = [9, 3, 2, 8, 5, 7, 1, 6]
print(insertion_sort(my_list))
