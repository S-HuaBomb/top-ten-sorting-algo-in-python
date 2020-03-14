import time
from randint_list import randint_list


def timer(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        time_cost = t2 - t1
        print(f'{func.__name__} 花费时间{time_cost}')
    return wrapper


def binary_search(arr, current):
    """折半查找"""
    low = 0
    high = len(arr)
    while low < high:
        mid = low + ((high - low) >> 1)  # 位运算逼格高，右移一位即除以2
        # mid = (low + high) / 2  # 加法在数据量大时有溢出风险
        # mid = low + (high - low) / 2  # 逼格不够高
        if arr[mid] > current:
            high = mid - 1
        elif arr[mid] < current:
            low = mid + 1
        else:
            return mid
    return -1


@timer
def bin_insert_sort(arr):
    """折半插入排序"""
    for i in range(1, len(arr)):
        index = binary_search(arr[:i + 1], arr[i])
        if index != i:
            arr[i], arr[index] = arr[index], arr[i]
    # print(arr)
    return arr


@timer
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
    # print(arr)
    return arr


@timer
def insertionSort(arr):
    """参考资料中的代码"""
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    # print(arr)
    return arr


if __name__ == '__main__':
    """折半插入排序大约比直接插入排序快20倍，参考答案快100倍。。。"""
    li = randint_list(start=0, stop=1e6, length=1000)
    print(li)
    insert_sort(li)
    bin_insert_sort(li)
    insertionSort(li)
    # print(insert_sort(li))
    # print(bin_insert_sort(li))
