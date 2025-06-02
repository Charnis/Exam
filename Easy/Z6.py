m = []
s, sr, result = 0, 0, 0
n = int(input("Введите количество значение в массиве: "))
for i in range(n):
    m.append(int(input(f"Введите {i+1}-ое значение: ")))
    s += 1
    sr += m[i]
    result = sr / s
print(result)
