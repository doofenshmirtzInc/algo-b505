# Author: Jack McShane
# CSCI-B505: Applied Algorithms
# Lab 4: Merge Sort
#
#
#
import sys
#sys.setrecursionlimit(10000)


def merge_sort(unsorted, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2
    #mid = (left + right) // 2
    #call merge_sort() on first half
    merge_sort(unsorted, left, mid)
    #call merge_sort() on second half
    merge_sort(unsorted, mid + 1, right)
    #merge the two arrays
    merge(unsorted, left, mid, right)


def merge(unsorted, left, mid, right):
    indexlh = 0
    indexrh = 0
    index_sortd = left
    left_half = unsorted[left:mid + 1]
    right_half = unsorted[mid + 1:right + 1]

    #while not out of elems in either array
    while indexlh < len(left_half) and indexrh < len(right_half):
        #if left elem < right add left elem to arr
        #else add right elem to array
        if left_half[indexlh] <= right_half[indexrh]:
            unsorted[index_sortd] = left_half[indexlh]
            indexlh += 1
        else:
            unsorted[index_sortd] = right_half[indexrh]
            indexrh += 1
        index_sortd += 1

    #once out of elements in one half of the passed arra
    #the next two for loops are used to copy the elements from whichever
    #half ran out of elements to the end of the newly sorted array
    while left_half:
        sortd.append(left_half.pop(0))

    while right_half:
        sortd.append(right_half.pop(0))



#read in the unsorted array len and the unsorted array
infile = sys.stdin.readlines()
alen = int(infile[0]) # not needed for python implementation
a = [int(elem) for elem in infile[1].split()]

#print('input:')
#print(*a)
merge_sort(a, 0, len(a) - 1)
#print('sorted array:')
print(*a)


