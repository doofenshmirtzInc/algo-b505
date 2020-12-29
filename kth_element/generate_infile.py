import random as r

size = r.randint(1,11)

array = []
for i in range(0, size):
    array.append(r.randint(-10,10))


print(size)
print(*array)
print(r.randint(1, size))

