from randint_list import randint_list


def counting_sort(arr):
    """
    计数排序，将元素值作为数组下标

    :bucket_len:
    :max_value: 需要指明待排数组的最大元素值
    """
    bucket_len = max(arr) + 1
    bucket = [0] * bucket_len
    sorted_index = 0
    arr_len = len(arr)
    for i in range(arr_len):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucket_len):
        while bucket[j] > 0:
            arr[sorted_index] = j
            sorted_index += 1
            bucket[j] -= 1
    return arr


if __name__ == '__main__':
    li = randint_list()
    max_value = max(li)
    print(li, f'max_value: {max_value}')
    print(counting_sort(li))
