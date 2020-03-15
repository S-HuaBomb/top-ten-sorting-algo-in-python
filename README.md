# top-ten-sorting-algo-in-python
用 python 手撸十大排序算法

## 目录
* [冒泡排序](#1-冒泡排序)
* [选择排序](#2-选择排序)
* [插入排序](#3-插入排序)

## 1. 冒泡排序
### 算法步骤
1. 比较相邻的元素。比如第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
### 动图演示
![bubble](https://img-blog.csdnimg.cn/20200314230014948.gif)
### Python 代码
```python
def bubble_sort(arr):
    """冒泡排序"""
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
* [返回目录](#目录)
---

## 2. 选择排序
### 算法步骤
1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。
### 动图演示
![selection](https://img-blog.csdnimg.cn/20200314230034422.gif)
### Python 代码
```python
def selection_sort(arr):
    """选择排序"""
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```
* [返回目录](#目录)
---

## 3. 插入排序
### 算法步骤
1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
### 动图演示
![insertion](https://img-blog.csdnimg.cn/20200314230819723.gif)
### Python 代码
```python
def insertionSort(arr):
    """插入排序"""
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex + 1] = current
    return arr
```
* [返回目录](#目录)
---

## 4. 希尔排序
### 算法步骤
1. 选择一个增量序列 $ t_1, t_2, t_i, ..., t_j, t_k $，其中 $ t_i > t_j $, $ t_k = 1 $；
2. 按增量序列个数 k，对序列进行 k 趟排序；
3. 每趟排序，根据对应的增量 $ t_i $，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，
整个序列作为一个表来处理，表长度即为整个序列的长度。
### Python 代码
```python
def shell_sort(arr):
    """希尔排序"""
    import math
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
    return arr
```
* [返回目录](#目录)
---
