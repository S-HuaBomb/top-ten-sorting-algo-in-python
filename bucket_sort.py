from randint_list import randint_list
from insert_sort import insert_sort


def bucket_sort(arr):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    bucket_size = (max_num - min_num) / len(arr)  # 桶的大小
    count_list = [[] for _ in range(len(arr) + 1)]  # 桶数组
    # 向桶数组填数
    for i in arr:
        count_list[int((i - min_num) // bucket_size)].append(i)
    arr.clear()
    # 回填，这里桶内部排序调用了 insert_sort()
    print(count_list)
    for i in count_list:
        for j in insert_sort(i):
            arr.append(j)
    return arr


if __name__ == "__main__":
    li = randint_list()
    print(li)
    print(bucket_sort(li))
