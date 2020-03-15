from randint_list import randint_list


def build_max_heap(arr):
    """建大顶堆堆, 调用 heapify()"""
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i)


def heapify(arr, i):
    """把最大元素推到堆顶"""
    left = 2 * i + 1  # 左节点
    right = 2 * i + 2  # 右节点
    largest = i
    if left < arr_len and arr[left] > arr[largest]:
        largest = left
    if right < arr_len and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def heap_sort(arr):
    """堆排序"""
    global arr_len
    arr_len = len(arr)
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        arr_len -= 1
        heapify(arr, 0)
    return arr


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    li = randint_list()
    print(li)
    res = heap_sort(li)
    print(res)
