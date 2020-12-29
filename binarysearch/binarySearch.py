#Jack McShane
#CSCI-B505 Applied Algorithms
#lab 3: Binary Search

#bug might have to do with the len calculations for the arrays


import sys


########################METHOD DEF##########################
def bin_search(query, a, low, high):
    if low > high:
        return -1

    mid = low + (high - low) // 2
    if a[mid] == query:
        return mid + 1
    elif query < a[mid]:
        return bin_search(query, a, low, mid - 1)
    else:
        return bin_search(query, a, mid + 1, high)


#########################TEST CODE###########################
infile = sys.stdin.readlines()
n = int(infile[0])  #not needed for python implementation
m = int(infile[1])  #not needed for python implementation
arr = [int(elem) for elem in infile[2].split()]
query = [int(elem) for elem in infile[3].split()]
res = []

for elem in query:
    res.append(bin_search(elem, arr, 0, len(arr) - 1))

print(*res)

