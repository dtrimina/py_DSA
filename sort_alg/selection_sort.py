#coding:utf8

'''selection sort algorithm with python3'''

from data import data1, data2, data3


def selection_sort(arr):
    '''遍历数组每次将未排序部分的最小值放到已排序部分的最后面，直到所有数排序完成'''
    if len(arr) <= 1: return arr
    for i in range(len(arr) - 1):
        smallest_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


if __name__ == '__main__':
    print('data1: {}'.format(data1))
    print('data2: {}'.format(data2))
    print('data3: {}'.format(data3))
    print('after sorted:' + '='*120)
    print('data1: {}'.format(selection_sort(data1)))
    print('data2: {}'.format(selection_sort(data2)))
    print('data3: {}'.format(selection_sort(data3)))