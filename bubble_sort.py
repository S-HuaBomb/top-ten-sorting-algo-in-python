def bubble_sort(arr):
    """冒泡排序"""
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    li = [1, 3, 7, 4, 2, 5, 9, 8, 6]
    print(bubble_sort(li))
