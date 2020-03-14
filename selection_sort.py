from randint_list import randint_list


def selection_sort(arr):
    """选择排序"""
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    li = randint_list()
    print(li)
    print(selection_sort(li))

