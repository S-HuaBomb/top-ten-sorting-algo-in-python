import time


def timer(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        t1 = time.time()
        func(*args, **kwargs)
        t2 = time.time()
        time_cost = t2 - t1
        print(f'{func.__name__} 花费时间 {time_cost}')
    return wrapper
