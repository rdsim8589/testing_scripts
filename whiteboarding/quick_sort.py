#!/usr/bin/python3
"""
implement quick sort
"""
def sort(first, last, ary):
    pivot = ary[first]
    i = first
    j = last
    while i < j:
        print("i: {}, j:{}".format(i,j))
        if ary[i] < pivot:
            i += 1
        if ary[j] > pivot:
            j -= 1
        if ary[i] >= pivot and ary[j] <= pivot:
            num_hold = ary[i]
            ary[i] = ary[j]
            ary[j] = num_hold
            i += 1
            j -= 1
    return i

def quickSort(first, last, ary):
    if first < last:
        mid = sort(first, last, ary)
        print(mid)
        quickSort(first, mid - 1, ary)
        quickSort(mid, last, ary)


ary = [4, 23, 12, -1, 24, 5, -3]
print("before sort: {}".format(ary))
quickSort(0, len(ary) - 1, ary)
print("after sort: {}".format(ary))
