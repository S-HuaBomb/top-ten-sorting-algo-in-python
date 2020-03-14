# top-ten-sorting-algo-in-python
用 python 手撸十大排序算法

* [冒泡排序](#1-冒泡排序)
  * [算法步骤](#算法步骤)
  * [动图演示](#动图演示)
  * [python代码](#python-代码)

## 1. 冒泡排序
### 算法步骤
1. 比较相邻的元素。比如第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
### 动图演示
![bubble](https://user-images.githubusercontent.com/39048551/76676661-c9ce6000-6600-11ea-9ae5-8269cf346f79.gif)
### Python 代码
```python
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```
