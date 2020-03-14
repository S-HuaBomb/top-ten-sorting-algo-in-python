import random


def randint_list(start=0, stop=20, length=7):
    """生成随机整数列表"""
    rand_list = []
    length = int(length)
    if length > 0:
        start, stop = sorted((start, stop))
        for _ in range(length):
            rand_list.append(random.randint(start, stop))
    elif length <= 0:
        return None
    return rand_list
