#coding:utf8

'''merge sort algorithm with python3'''

from data import data1, data2, data3


def _do_merge(arr, lo, mid, hi):
    '''先将arr[lo: mid]和arr[mid+1: hi]按真确顺序排好存储到arr_storage,
       然后再转移到arr[lo: hi]中'''
    arr_storage = []
    i = lo
    j = mid + 1
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            arr_storage.append(arr[i])
            i += 1
            continue
        else:
            arr_storage.append(arr[j])
            j += 1
    while i <= mid:
        arr_storage.append(arr[i])
        i += 1
    while j <= hi:
        arr_storage.append(arr[j])
        j += 1

    for i in range(lo, hi+1):
        arr[i] = arr_storage[i - lo]


def _do_sort(arr, lo, mid, hi):
    if lo >= hi: return
    _do_sort(arr, lo, (lo+mid)//2, mid)
    _do_sort(arr, mid+1, (mid+1+hi)//2, hi)
    _do_merge(arr, lo, mid, hi)
    return arr


def merge_sort(arr):
    if len(arr) <= 1: return
    return _do_sort(arr, 0, (len(arr)-1)//2, len(arr)-1)


if __name__ == '__main__':
    print('data1: {}'.format(data1))
    print('data2: {}'.format(data2))
    print('data3: {}'.format(data3))
    print('after sorted:' + '='*120)
    print('data1: {}'.format(merge_sort(data1)))
    print('data2: {}'.format(merge_sort(data2)))
    print('data3: {}'.format(merge_sort(data3)))
