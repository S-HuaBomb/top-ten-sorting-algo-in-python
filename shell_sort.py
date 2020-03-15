import math
from randint_list import randint_list


def shell_sort(arr):
    """希尔排序"""
    gap = 1
    step = math.sqrt(len(arr))
    while gap < step:
        gap = int(gap * step + 1)
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap = int(gap // step)  # 下取整
    print(arr)
    return arr


if __name__ == '__main__':
    li = randint_list(0, 1e6, 10000)
    print(li)
    shell_sort(li)
    # print(9 // 3.0)  # 3.0
