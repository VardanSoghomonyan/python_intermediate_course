arr = [15, 26, 33, 45, 57, 68]
a = 57


def binary_search(provided_list, n):
    min_index = 0
    max_index = len(provided_list) - 1

    while min_index <= max_index:
        mid = (min_index + max_index) // 2
        if provided_list[mid] < n:
            min_index = mid + 1
        elif provided_list[mid] > n:
            max_index = mid - 1
        else:
            return mid
    return -1


result = binary_search(arr, a)
if result != -1:
    print("Element exists in index", result)
else:
    print("Element doesn't exist in the provided list")
