import random

a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
c = [num for num in set(a) if num in b]
print(a)
print(b)
print(c)

