import random


def reorder(arr):
    reordered = []
    while len(arr) > 0:
        r = random.randint(0, len(arr)-1)
        reordered.append(arr[r])
        arr.remove(arr[r])
    return reordered

#test code
a = [random.randint(1, 50)]
for j in range(20):
    a.append(random.randint(0, 50))
print(a)

new_arr = reorder(a)
print(new_arr)
