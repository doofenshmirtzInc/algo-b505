import sys

def fib(n):
    if n == 0:
        return 0

    numbers = [0, 1]
    #unless I am missing something, you have to start at i = 2
    #starting at i = 1 will give an erratic answer when numbers[i-2] is
    #referenced
    for i in range(2, n+1):
        numbers.append(numbers[i-1] + numbers[i-2])

    return numbers[-1]


infile = sys.stdin.readlines()
numbers = []

for line in infile:
    numbers.append(int(line))

for elem in numbers:
    print(fib(elem))


