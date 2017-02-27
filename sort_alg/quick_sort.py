#coding:utf8

'''quick sort algorithm with python3'''

from data import data1, data2, data3


def _get_index(arr, lo, hi):
    '''将arr[lo]排到真确的位置并将正确位置返回'''
    s = arr[lo]
    status = 2

    while lo < hi:
        if arr[hi] < s and status == 2:
            arr[lo] = arr[hi]
            status = 1
            continue
        elif arr[hi] >= s and status == 2:
            hi -= 1
        elif arr[lo] > s and status == 1:
            arr[hi] = arr[lo]
            status = 2
        else:
            lo += 1
    arr[lo] = s
    return lo


def _do_quick_sort(arr, lo, hi):
    if lo >= hi: return
    label = _get_index(arr, lo, hi)
    _do_quick_sort(arr, lo, label - 1)
    _do_quick_sort(arr, label + 1, hi)
    return arr


def quick_sort(arr):
    if len(arr) <= 1: return
    return _do_quick_sort(arr, 0, len(arr)-1)


if __name__ == '__main__':
    print('data1: {}'.format(data1))
    print('data2: {}'.format(data2))
    print('data3: {}'.format(data3))
    print('after sorted:' + '='*120)
    print('data1: {}'.format(quick_sort(data1)))
    print('data2: {}'.format(quick_sort(data2)))
    print('data3: {}'.format(quick_sort(data3)))
