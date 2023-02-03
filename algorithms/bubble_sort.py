def bubble_sort(list):
    n = len(list)
    for item in range(1, n - 1):
        for jtem in range(n - item):
            if list[jtem] > list[jtem + 1]:
                temp = list[jtem]
                list[jtem] = list[jtem + 1]
                list[jtem + 1] = temp
    return list

numbers = [4, 5, 2, 66, 44, 1, 3]
assert(bubble_sort(numbers) == [1, 3, 2, 3, 4, 5, 44, 66])
