arr = [15, 26, 33, 45, 57, 68]
a = 57


def binary_search(provided_list, low, high, n):
    if low <= high:
        mid = (low + high) // 2

        if provided_list[mid] == n:
            return mid
        elif provided_list[mid] > n:
            return binary_search(provided_list, low, mid - 1, n)
        else:
            return binary_search(provided_list, mid + 1, high, n)
    else:
        return -1


result = binary_search(arr, 0, len(arr) - 1, a)
if result != -1:
    print("Element exists in index", result)
else:
    print("Element doesn't exist in the provided list")
