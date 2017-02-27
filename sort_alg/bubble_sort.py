#coding:utf8

'''bubble sort algorithm with python3'''

from data import data1, data2, data3


def bubble_sort(arr):
    '''每一次扫描将大的数往后挪，直到所有的数真确排序'''
    if len(arr) <= 1: return arr
    time = len(arr) - 1
    while time:
        for i in range(time):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        time -= 1
    return arr

if __name__ == '__main__':
    print('data1: {}'.format(data1))
    print('data2: {}'.format(data2))
    print('data3: {}'.format(data3))
    print('after sorted:' + '='*120)
    print('data1: {}'.format(bubble_sort(data1)))
    print('data2: {}'.format(bubble_sort(data2)))
    print('data3: {}'.format(bubble_sort(data3)))