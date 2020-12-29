import sys
import random as r


def selection(array, k):
    ###########base case:
    #maybe????
    if len(array) == 1:
        return array[0]

    ############selection
    subl = []
    subv = []
    subr = []
    v = array[r.randint(0, len(array) - 1)]
    for i in range(0, len(array)):
        if array[i] == v:
            subv.append(array[i])
        elif array[i] < v:
            subl.append(array[i])
        else:
            subr.append(array[i])

    #check k against length of subarrrays
    if k <= len(subl):
        return selection(subl, k)
    elif (k - len(subl)) <= len(subv):
        return selection(subv, k - len(subl))
    else:
        return selection(subr, (k - len(subl) - len(subv)))














#driver code
infile = sys.stdin.readlines()
array = [int(elem) for elem in infile[1].split()]
k = int(infile[2])

print(selection(array, k))
