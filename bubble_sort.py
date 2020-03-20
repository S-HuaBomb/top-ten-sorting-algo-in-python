import time
from randint_list import randint_list


def timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__} 花费时间 {t2 - t1}")
    return wrapper


@timer
def bubble_sort(arr):
    """冒泡排序"""
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@timer
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


@timer
def bubble_sort_(origin_items, comp=lambda x, y: x > y):
    """高质量冒泡排序(搅拌排序)"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


if __name__ == '__main__':
    """其实最朴素的冒泡排序在随机数列的情况下是最快的"""
    # li = [1, 3, 7, 4, 2, 5, 9, 8, 6]
    li = randint_list(0, 1e6, 10000)
    print(li)
    bubble_sort(li)
    # bubbleSort(li)
    # bubble_sort_(li)
