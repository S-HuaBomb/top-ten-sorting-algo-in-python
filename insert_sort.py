from randint_list import randint_list
from timer import timer


def binary_search(arr, current):
    """折半查找
    前提是 array 已经有序
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)  # 位运算逼格高，右移一位即除以2
        # mid = (low + high) / 2  # 加法在数据量大时有溢出风险
        # mid = low + (high - low) / 2  # 逼格不够高
        if arr[mid] > current:
            high = mid - 1
        elif arr[mid] < current:
            low = mid + 1
        else:
            break
    return low


# @timer
def bin_insert_sort(arr):
    """折半插入排序"""
    for i in range(1, len(arr)):
        current = arr[i]  # 注意暂存的重要性，因为移动元素的时候arr[i]会被覆盖掉
        index = binary_search(arr[:i], arr[i])
        for j in range(i, index, -1):
            arr[j] = arr[j - 1]
        arr[index] = current
    print(arr)
    return arr


# @timer
def insert_sort(arr):
    """插入排序"""
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i, -1, -1):  # 此前的序列已经有序，需要从后往前比较
            if arr[j - 1] > temp:
                arr[j] = arr[j - 1]  # 元素右移
            else:
                break
        arr[j] = temp  # 插入
    print(arr)
    return arr


# @timer
def insertionSort(arr):
    """参考资料中的代码"""
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    print(arr)
    return arr


def binaryInsert(arr):
    # 折半插入排序: 小->大
    # 在直接插入排序的基础上使用了折半查找的方法
    for i in range(1, len(arr)):
        index = arr[i]
        low = 0
        high = i - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if index > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        # 跳出循环后 low, mid 都是一样的,其实不一样 hight = low - 1
        for j in range(i, low, -1):
            # print(j)
            arr[j] = arr[j - 1]
        arr[low] = index
    print(arr)
    return arr


if __name__ == '__main__':
    li = randint_list(start=0, stop=1e6, length=10000)
    # li = [6, 3, 1, 2, 5, 7, 4]
    # print(li)
    # insert_sort(li)
    # bin_insert_sort(li)
    insertionSort(li)
    # binary_search(li, 5)
