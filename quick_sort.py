import time
from randint_list import randint_list


def quick_sort(arr, left=None, right=None):
    """快速排序"""
    left = 0 if left is None else left  # 第一次递归调用时的初值
    right = len(arr) - 1 if right is None else right  # 第一次递归调用时的初值
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[left]  # 第一个元素作为枢纽
    while left < right:  # left == right 时跳出
        while left < right and arr[right] >= pivot:
            # 从右往左找到第一个比 pivot 小的元素的下标
            right -= 1
        arr[left] = arr[right]  # 将其放到 pivot 左边
        while left < right and arr[left] <= pivot:
            # 从左往右找到第一个比 pivot 大的元素的下标
            left += 1
        arr[right] = arr[left]  # 将其放到 pivot 右边
    arr[left] = pivot  # 此时left、right两个指针指向相同位置
    return left


if __name__ == '__main__':
    li = randint_list(0, 1e6, 10000)
    print(li)
    # t1 = time.time()
    res = quick_sort(li)
    # t2 = time.time()
    print(res)
    # print(t2 - t1)
