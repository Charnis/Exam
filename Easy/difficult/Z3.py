import random
m = []
n = int(input())
a = random.randint(1, n-1)
b = 0
for i in range(1, n+1):
    m.append(i)
m.pop(a)
print(m)
try:
    for j in range(n):
        b += 1
        if b != m[j]:
            print(f"Число {b} отсутствует")
            break
except IndexError:
    print(f"Число {n} отсутствует")