#author: jack mcshane
#this program is an implementation of the max heap data structure

import sys



# returns max-heap of given elements
# -input: array of size n
# -output: max-heap of size n
#
def max_heapify(array, i):
    left = 2*i + 1
    right = 2*i + 2
    if left < len(array) and array[left] > array[i]:
        largest = left
    else:
        largest = i
    if right < len(array) and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)


def build_max_heap(array):
    last_parent = (len(array)//2) - 1
    for i in range(last_parent, -1, -1):
        max_heapify(array, i)


#driver code
infile = sys.stdin.readlines()
n = int(infile[0])  #not needed for python implementation
elements = [int(elem) for elem in infile[1].split()]

build_max_heap(elements)
print(*elements)
