#jack mcshane
#CSCI-B505 Applied Algorithms
#lab 2: insertion sort

import sys

def insertion_sort(a):
    num_swaps = 0
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while key < a[i] and i >= 0:
            num_swaps += 1
            a[i + 1] = a[i]
            i -= 1
        a[i+1] = key
    return num_swaps


infile = sys.stdin.readlines()
alen = int(infile[0]) # not needed for implementation
a = [int(elem) for elem in infile[1].split()]

print(insertion_sort(a))

