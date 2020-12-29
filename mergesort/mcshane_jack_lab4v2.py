import sys

def ms(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    #print(f'ms(array[0:mid]), array: {array[0:mid]}')
    left_half = ms(array[0:mid])
    #print(f'left_half: {left_half}')
    #print(f'ms(array[mid:len(array)]): {array[mid:len(array)]}')
    right_half = ms(array[mid:len(array)])
    #print(f'right_half: {right_half}')
    sortd = merge(left_half, right_half)
    #print(f'sortd: {sortd}')
    return sortd


def merge(left_half, right_half):
    #assumed: left_half and right_half are sortd
    sortd = []
    while left_half and right_half:
        left = left_half[0]
        right = right_half[0]
        if left <= right:
            sortd.append(left_half.pop(0))
        else:
            sortd.append(right_half.pop(0))

        #move rest of left_half and right_half to end of sortd
    #could have just done:
    #sortd.extend(left_half)
    #sortd.extend(right_half)
    #return sorted
    while left_half:
        sortd.append(left_half.pop(0))

    while right_half:
        sortd.append(right_half.pop(0))

    return sortd



#driver code
infile = sys.stdin.readlines()
alen = int(infile[0])
a = [int(elem) for elem in infile[1].split()]

sorted_array = ms(a)
#print('sorted array:')
print(*sorted_array)
