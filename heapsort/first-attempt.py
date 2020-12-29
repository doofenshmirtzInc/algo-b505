#author: jack mcshane
#this program is an implementation of the max heap data structure

import sys



# returns max-heap of given elements
# -input: array of size n
# -output: max-heap of size n
#
def max_heapify(array, heapsize, i):
    left = 2*i + 1
    right = 2*i + 2
    if left < heapsize and array[left] > array[i]:
        largest = left
    else:
        largest = i
    if right < heapsize and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, heapsize, largest)


def build_max_heap(array):
    last_parent = (len(array)//2) - 1
    for i in range(last_parent, -1, -1):
        max_heapify(array, len(array), i)


def heapsort(array):
    build_max_heap(array)
    heapsize = len(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapsize -= 1
        max_heapify(array, heapsize, 0)


#driver code
infile = sys.stdin.readlines()
n = int(infile[0])  #not needed for python implementation
elements = [int(elem) for elem in infile[1].split()]

heapsort(elements)
print(*elements)
