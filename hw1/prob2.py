import sys

def code(arr):
    n = len(arr)
    for j in range(1, n - 1):
        if arr[n - 1] < arr[j]:
            temp = arr[j]
            arr[j] = arr[n - 1]
            arr[n - 1] = temp



arr = []
infile = sys.stdin.readlines()
for line in infile:
    arr.append(int(line))

print(f'before code applied: {arr}')

code(arr)
print(f'after code applied: {arr}')
