target = int(input())
m = [-9, -8, -7, -6, -5, -4, -3, -2, 1, 0, 1, 2, 3, 6, 4, 5, 7, 8, 9]
g = 1
for i in range(1, len(m)):
    for j in range(0, len(m)):
        b = m[i - 1] + m[j]
        if m[i - 1] == m[j]:
            print("", end='')
        else:
            if b == target and g == 1:
                print(f"{m[i - 1]} + {m[j]} = {b}")
                print(f"Сумма чисел {m[i - 1]} и {m[j]} равна {target}")
                g = 0
                break
        if g == 0:
            break
