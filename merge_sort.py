from randint_list import randint_list  # 随机整数列
from timer import timer  # 计时装饰器


def merge_sort(arr):
    """归并排序"""
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def merge_sort_(arr):
    """归并排序"""
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    return merge_(merge_sort(left), merge_sort(right))


def merge_(left, right):
    """双指针"""
    result = []
    index1, index2 = 0, 0
    while index1 < len(left) and index2 < len(right):
        if left[index1] < right[index2]:
            result.append(left[index1])
            index1 += 1
        else:
            result.append(right[index2])
            index2 += 1
    result.append(left[index1:])
    result.append(right[index2:])
    return result


# @timer
def main(arr):
    li = merge_sort_(arr)
    return li


if __name__ == '__main__':
    li = randint_list(0, 1e6, 10000)
    # print(len(li))
    # merge_sort(li)
    res = main(li)
    print(res)
