#coding:utf8

'''insertion sort algorithm with python3'''

from data import data1, data2, data3


def insertion_sort(arr):
    '''arr从投开始依次扫描，每次扫描将当前位置后一个元素插入到之前序列中正确的位置'''
    if len(arr) <= 1: return arr
    for i in range(len(arr) - 1):
        k = arr[i + 1]
        j = i
        while arr[j] > k and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr


if __name__ == '__main__':
    print('data1: {}'.format(data1))
    print('data2: {}'.format(data2))
    print('data3: {}'.format(data3))
    print('after sorted:' + '='*120)
    print('data1: {}'.format(insertion_sort(data1)))
    print('data2: {}'.format(insertion_sort(data2)))
    print('data3: {}'.format(insertion_sort(data3)))
