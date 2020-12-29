#Author: jack mcshane
#Applied Alogorithms
#lab 5/6: quicksort algorithm



import sys
import random as r


def randQS(array, left, right):
    if left >= right:
        return

    k = r.randint(left, right)
    #swapping elements
    swap(array, left, k)

    m = partition(array, left, right)
    randQS(array, left, m - 1)
    randQS(array, m + 1, right)



def partition(array, left, right):
    x = array[left] #this is the pivot
    j = left
    for i in range(left + 1, right + 1):
        if array[i] <= x:
            j += 1
            swap(array, j, i)
            #swap a[j] and a[i]
    #swap a[left] and a[j]
    swap(array, left, j)
    return j


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp





#driver code
infile = sys.stdin.readlines()
array = [int(elem) for elem in infile[1].split()]


randQS(array, 0, len(array) - 1)
print(*array)
