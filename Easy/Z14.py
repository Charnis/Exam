import random
m = []
a, b = 0, 0
for i in range(15):
    m.append(random.randint(-10,10))
    if m[i] > 0:
        a += 1
    else:
        b += 1
print(m)
print(f"Количесво положительных чисел = {a}")
print(f"Количесво отрицательных чисел = {b}")