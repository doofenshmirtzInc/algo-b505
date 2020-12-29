#Author: jack mcshane
#Applied Algorithms FA 2020
#Majority Element
import sys

#returns: number of times elem occurs in arr
def freq(elem, arr):
    if len(arr) == 1:
        return 1 if arr[0] == elem else 0

    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    return (freq(elem, left) + freq(elem, right))



#returns: a tuple (m,f) where m is the majority element in arr
#and f is the frequency with which it occurs
def majority(arr):
    if len(arr) == 1:
        return (arr[0], 1)

    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    (maj_left, freq_left) = majority(left)
    #if there is a majority element in the left half of arr
    if maj_left != -1:
        #count the times it occurs in arr
        freq_left += freq(maj_left, right)
        #if it is a majority element in the entire array arr
        if freq_left > mid:
            #return tuple
            return (maj_left, freq_left)

    (maj_right, freq_right) = majority(right)
    #mirrors above code
    if maj_right != -1:
        freq_right += freq(maj_right, left)
        if freq_right > mid:
            return (maj_right, freq_right)

    #if no majority element in arr, return tuple
    return (-1, 0)





#driver code
infile = sys.stdin.readlines()
#infile is a list of strings, one for each line
arrays = []
for line in infile:
    arr = [int(elem) for elem in line.split()]
    arrays.append(arr)

#this line is not needed in python implementation
arrays.pop(0)

majority_elems = []
for array in arrays:
    majority_elems.append(majority(array)[0])

print(*majority_elems)
