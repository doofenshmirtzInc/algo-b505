import random
#pseudocode
#arr as input
#arrlen = len(arr)
#declare new array of size arrlen
#loop thru array w/ j
    #r = rand(0, 3*arrlen) % arrlen
    #while arr[r] != 0 and r
        #r++
    #newarr[r] = arr[j]


def reorder(arr):
    arr_len = len(arr)
    rand_arr = [0] * arr_len
    for i in range(0, arr_len):
        r = random.randint(0, 3 * arr_len) % arr_len
        while rand_arr[r] != 0:
            if r >= arr_len: r = 0
            else: r += 1
        rand_arr[r] = arr[i]
    return rand_arr



#test code
a = [random.randint(1, 50)]
for j in range(20):
    a.append(random.randint(0, 50))
print(a)

new_arr = reorder(a)
print(new_arr)
