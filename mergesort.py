# import libraries at the start
import matplotlib.pyplot as plt

def merge_sort(list_to_sort):
    # check if list has at least two elements and split into left_list and right_list
    if (len(list_to_sort) > 1):
        mid = len(list_to_sort) // 2
        left_list = list_to_sort[:mid]
        right_list = list_to_sort[mid:]

        # call function recursively for left_list and right_list
        merge_sort(left_list)
        merge_sort(right_list)

        l = 0
        r = 0
        i = 0

        # go through elements in left_list and right_list
        while l < len(left_list) and r < len(right_list):
            # compare element of left_list with right_list
            # if element from left_list is smaller, pick this one
            if left_list[l] <= right_list[r]:
                list_to_sort[i] = left_list[l]
                l += 1
            # otherwise, pick the one from the right_list
            else:
                list_to_sort[i] = right_list[r]
                r += 1
            i += 1

        # write elements from left_list into list_to_sort, starting with position l
        while l < len(left_list):
            list_to_sort[i] = left_list[l]
            l += 1
            i += 1

        # write elements from right_list into list_to_sort, starting with position r
        while r < len(right_list):
            list_to_sort[i] = right_list[r]
            r += 1
            i += 1

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plt.plot(my_list)
plt.show()
merge_sort(my_list)
plt.plot(my_list)
plt.show()
