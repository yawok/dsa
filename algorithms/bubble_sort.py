# 03/02/23
# bubble sort algorithm 

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
numbers1 = [4, 5]
numbers2 = [10, 10, 10, 10, 10]
numbers3 = [100000, 33.4, 1, -47, -3]
assert bubble_sort(numbers) == [1, 2, 3, 4, 5, 44, 66]
assert bubble_sort(numbers1) == [4, 5]
assert bubble_sort(numbers2) == [10, 10, 10, 10, 10]
assert bubble_sort(numbers3) == [-47, -3, 1, 33.4, 100000]
