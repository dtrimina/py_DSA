#coding:utf8

'''heap sort algorithm with python3'''

from data import data1, data2, data3


def _ajust_heap(arr, i, size):
    '''将arr的i节点以下孩子部分实现最大堆的序列化'''
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max_id = i
    if i < size / 2:
        if lchild < size and arr[lchild] > arr[max_id]:
            max_id = lchild
        if rchild < size and arr[rchild] > arr[max_id]:
            max_id = rchild
        if max_id != i:
            arr[i], arr[max_id] = arr[max_id], arr[i]
            _ajust_heap(arr, max_id, size)


def _build_heap(arr, size):
    '''将arr所有的非叶子节点从下自上依次实现局部的最大堆，即实现初始化最大堆'''
    for i in range(0, size / 2)[::-1]:
        _ajust_heap(arr, i, size)


def heap_sort(arr):
    if len(arr) <= 1: return arr
    size = len(arr)
    _build_heap(arr, size)  #初始化最大堆
    for i in range(0, size)[::-1]:  #依次将最大元素排到后面然后实现剩余部分的最大堆
        arr[0], arr[i] = arr[i], arr[0]
        _ajust_heap(arr, 0, i)
    return arr


if __name__ == '__main__':
    print('data1: {}'.format(data1))
    print('data2: {}'.format(data2))
    print('data3: {}'.format(data3))
    print('after sorted:' + '='*120)
    print('data1: {}'.format(heap_sort(data1)))
    print('data2: {}'.format(heap_sort(data2)))
    print('data3: {}'.format(heap_sort(data3)))