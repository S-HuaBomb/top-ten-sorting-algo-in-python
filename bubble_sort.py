from randint_list import randint_list


def bubble_sort(arr):
    """冒泡排序"""
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSort(arr):
    """立 flag 的冒泡算法
    :param arr: 待排数组
    :return: 排好序的数组
    Examples:
    >>> bubbleSort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bubbleSort([])
    []
    >>> bubbleSort([-2, -5, -45])
    [-45, -5, -2]

    >>> bubbleSort([-23,0,6,-4,34])
    [-23,-4,0,6,34]
    """
    length = len(arr)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break  # 如果一趟下来没发生过交换，则说明已经排好序
    return arr


if __name__ == '__main__':
    # li = [1, 3, 7, 4, 2, 5, 9, 8, 6]
    li = randint_list()
    print(li)
    print(bubble_sort(li))
    print(bubbleSort(li))
