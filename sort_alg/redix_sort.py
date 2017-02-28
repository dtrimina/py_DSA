#coding:utf8

'''redix sort algorithm with python3'''

from data import data1, data2, data3


def redix_sort(arr, max_bit):
    '''基于桶排序，数字有低位向高位分别依次进行排序'''
    if len(arr) <= 1: return arr
    for k in range(max_bit):
        s = [[] for _ in range(10)]
        for i in arr:
            s[i//(10 ** k) % 10].append(i)
        arr = [a for b in s for a in b]
    return arr


if __name__ == '__main__':
    print('data1: {}'.format(data1))
    print('data2: {}'.format(data2))
    print('data3: {}'.format(data3))
    print('after sorted:' + '='*120)
    print('data1: {}'.format(redix_sort(data1, 1)))
    print('data2: {}'.format(redix_sort(data2, 2)))
    print('data3: {}'.format(redix_sort(data3, 3)))