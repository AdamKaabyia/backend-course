def first_element(lst):
    return lst[0]


my_list = [1, 2, 3, 4, 5]
print(first_element(my_list))


def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num


my_list = [3, 7, 2, 9, 5]
print(find_max(my_list))  # Output: 9


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


my_list = [2, 3, 5, 7, 9, 11, 13]
print(binary_search(my_list, 9))



