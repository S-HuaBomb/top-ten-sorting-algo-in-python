# top-ten-sorting-algo-in-python
用 python 手撸十大排序算法

## 目录
* [冒泡排序](#1-冒泡排序)
* [选择排序](#2-选择排序)
* [插入排序](#3-插入排序)
* [希尔排序](#4-希尔排序)
* [归并排序](#5-归并排序)
* [快速排序](#6-快速排序)
* [堆排序](#7-堆排序)
* [计数排序](#8-计数排序)
* [桶排序](#9-桶排序)
* [基数排序](#10-基数排序)

## 1. 冒泡排序
**冒泡排序**（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

作为最简单的排序算法之一，冒泡排序给我的感觉就像 Abandon 在单词书里出现的感觉一样，每次都在第一页第一位，所以最熟悉。
冒泡排序还有一种优化算法，就是立一个 flag，当在一趟序列遍历中元素没有发生交换，则证明该序列已经有序。
但这种改进对于提升性能来说并没有什么太大作用。
### 算法步骤
1. 比较相邻的元素。比如第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
### 动图演示
![bubble](https://img-blog.csdnimg.cn/20200314230014948.gif)
### [Python 代码](./bubble_sort.py)
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
**选择排序**是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。
唯一的好处可能就是不占用额外的内存空间了吧。
### 算法步骤
1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 重复第二步，直到所有元素均排序完毕。
### 动图演示
![selection](https://img-blog.csdnimg.cn/20200314230034422.gif)
### [Python 代码](./selection_sort.py)
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
**插入排序**的代码实现虽然没有冒泡排序和选择排序那么简单粗暴，但它的原理应该是最容易理解的了，因为只要打过扑克牌的人都应该能够秒懂。
插入排序是一种最简单直观的排序算法，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

插入排序和冒泡排序一样，也有一种优化算法，叫做[拆半插入](./insert_sort.py)。
### 算法步骤
1. 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
2. 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
### 动图演示
![insertion](https://img-blog.csdnimg.cn/20200314230819723.gif)
### [Python 代码](./insert_sort.py)
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
**希尔排序**，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

希尔排序是基于插入排序的以下两点性质而提出改进方法的：

* 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；
* 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位；

希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
### 算法步骤
1. 选择一个增量序列 $t_1, t_2, t_i, ..., t_j, t_k$，其中 $t_i > t_j$, $t_k = 1$；
2. 按增量序列个数 k，对序列进行 k 趟排序；
3. 每趟排序，根据对应的增量 $t_i$，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，
整个序列作为一个表来处理，表长度即为整个序列的长度。
### [Python 代码](./shell_sort.py)
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

## 5. 归并排序
**归并排序**（Merge sort）是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
作为一种典型的分而治之思想的算法应用，归并排序的实现由两种方法：

* 自上而下的递归（所有递归的方法都可以用迭代重写，所以就有了第 2 种方法）
* 自下而上的迭代

和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是 O(nlogn) 的时间复杂度。代价是需要额外的内存空间。
### 算法步骤
1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
4. 重复步骤 3 直到某一指针达到序列尾；
5. 将另一序列剩下的所有元素直接复制到合并序列尾。
### 动图演示
![merge](https://img-blog.csdnimg.cn/20200314231850999.gif)
![merge1](https://img-blog.csdnimg.cn/20200315163821851.gif)

### [Python 代码](./merge_sort.py)
```python
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
```
* [返回目录](#目录)
---

## 6. 快速排序
**快速排序**是由东尼·霍尔所发展的一种排序算法。在平均状况下，排序 n 个项目要 Ο(nlogn) 次比较。在最坏状况下则需要 Ο(n2) 次比较，
但这种状况并不常见。事实上，快速排序通常明显比其他 Ο(nlogn) 算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。

快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。快速排序又是一种分而治之思想在排序算法上的典型应用。
本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。

快速排序的名字起的是简单粗暴，因为一听到这个名字你就知道它存在的意义，就是快，而且效率高！它是处理大数据最快的排序算法之一了。
虽然 Worst Case 的时间复杂度达到了 O(n²)，但是人家就是优秀，在大多数情况下都比平均时间复杂度为 O(n logn) 的排序算法表现要更好，
可是这是为什么呢，我也不知道。好在我的强迫症又犯了，查了 N 多资料终于在《算法艺术与信息学竞赛》上找到了满意的答案：
> 快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，
> 比复杂度稳定等于 O(nlogn) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
### 算法步骤
1. 从数列中挑出一个元素，称为 “基准”（pivot）;
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，
该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

### 动图演示
![quick](https://img-blog.csdnimg.cn/20200314232839666.gif)
### [Python 代码](./quick_sort.py)
```python
def quick_sort(arr, left=None, right=None):
    """快速排序"""
    left = 0 if left is None else left  # 第一次递归调用时的初值
    right = len(arr) - 1 if right is None else right  # 第一次递归调用时的初值
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[left]  # 第一个元素作为枢纽
    while left < right:  # left == right 时跳出
        while left < right and arr[right] >= pivot:
            # 从右往左找到第一个比 pivot 小的元素的下标
            right -= 1
        arr[left] = arr[right]  # 将其放到 pivot 左边
        while left < right and arr[left] <= pivot:
            # 从左往右找到第一个比 pivot 大的元素的下标
            left += 1
        arr[right] = arr[left]  # 将其放到 pivot 右边
    arr[left] = pivot  # 此时left、right两个指针指向相同位置
    return left
```
* [返回目录](#目录)
---

## 7. 堆排序
**堆排序**（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：

* 大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
* 小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；

堆排序的平均时间复杂度为 Ο(nlogn)。
### 算法步骤
1. 创建一个堆 H[0……n-1]；
2. 把堆首（最大值）和堆尾互换；
3. 把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；
4. 重复步骤 2，直到堆的尺寸为 1。
### 动图演示
![heap1](https://img-blog.csdnimg.cn/20200315163806989.gif)
### [Python 代码](./heap_sort.py)
```python
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
```
* [返回目录](#目录)
---

## 8. 计数排序
**计数排序**的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
### 动图演示
![counting](https://img-blog.csdnimg.cn/2020031423293110.gif)
### [Python 代码](./counting_sort.py)
```python
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

```
* [返回目录](#目录)
---

## 9. 桶排序
**桶排序**是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：

* 在额外空间充足的情况下，尽量增大桶的数量
* 使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中

同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

**什么时候最快？**

当输入的数据可以均匀的分配到每一个桶中。
最快时间复杂度：O(n+k)

**什么时候最慢？**

当输入的数据被分配到了同一个桶中。
最坏时间复杂度：O(n<sup>2</sup>)

**平均时间复杂度：**O(n2)
### 动图演示
![bucket1](https://img-blog.csdnimg.cn/20200315163457248.png)
![bucket2](https://img-blog.csdnimg.cn/20200315163511987.png)
### [Python 代码](./bucket_sort.py)
```python
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
```
* [返回目录](#目录)
---

## 10. 基数排序
基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串
（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。

**基数排序 vs 计数排序 vs 桶排序**

这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：

* 基数排序：根据键值的每位数字来分配桶；
* 计数排序：每个桶只存储单一键值；
* 桶排序：每个桶存储一定范围的数值；
### 算法步骤
1. 比较相邻的元素。比如第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
### 动图演示
![radix](https://img-blog.csdnimg.cn/20200314232942531.gif)
### [Python 代码](./radix_sort.py)
```python
def radix_sort(arr):
    i = 0  # 初始为个位排序
    n = 1  # 最小的位数置为1（包含0）
    max_num = max(arr)  # 得到带排序数组中最大数
    while max_num > 10 ** n:  # 得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}  # 用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])  # 将每个桶置空
        for x in arr:  # 对每一位进行排序
            radix = int((x / (10 ** i)) % 10)  # 得到每位的基数
            bucket[radix].append(x)  # 将对应的数组元素加入到相 #应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:  # 若桶不为空
                for y in bucket[k]:  # 将该桶中每个元素
                    arr[j] = y  # 放回到数组中
                    j += 1
        i += 1
    return arr
```
* [返回目录](#目录)
