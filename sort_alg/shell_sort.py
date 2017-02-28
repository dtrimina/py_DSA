#coding:utf8

'''shell sort algorithm with python3'''

from data import data1, data2, data3


def shell_sort(arr):
    if len(arr) <= 1: return arr
    count = len(arr)
    group = count // 2
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                while k >= 0:
                    if arr[k] > arr[k + group]:
                        arr[k], arr[k + group] = arr[k + group], arr[k]
                    k -= group
                j += group
        group //= 2

    return arr


if __name__ == '__main__':
    print('data1: {}'.format(data1))
    print('data2: {}'.format(data2))
    print('data3: {}'.format(data3))
    print('after sorted:' + '='*120)
    print('data1: {}'.format(shell_sort(data1)))
    print('data2: {}'.format(shell_sort(data2)))
    print('data3: {}'.format(shell_sort(data3)))