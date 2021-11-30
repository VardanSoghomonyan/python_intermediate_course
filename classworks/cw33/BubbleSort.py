def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


def bubble_sort1(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


def bubble_sort2(list1):
    has_swapped = True

    while has_swapped:
        has_swapped = False
        for i in range(len(list1) - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True

    return list1


def bubble_sort3(list1):
    has_swapped = True
    total_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(list1) - total_iterations - 1):
            if list1[i] > list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True
        total_iterations += 1

    print("Total iterations: ", total_iterations)

    return list1


list_given = [5, 6, 2, 48]
print(bubble_sort3(list_given))
