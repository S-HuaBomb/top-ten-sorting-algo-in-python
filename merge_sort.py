from randint_list import randint_list


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


if __name__ == '__main__':
    li = randint_list()
    print(li)
    res = merge_sort(li)
    print(res)
