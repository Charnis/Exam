import random

a = random.randint(3, 10)
m = []
for i in range(1, a):
    m.append(random.randint(1, 100))
print(m)
maximum = max(m)
m.pop(m.index(maximum))
second_maximum = max(m)
print(second_maximum)
