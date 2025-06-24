m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X = int(input("Введите число для нахождения его в массиве: "))
for j in range(len(m)):
    if X == m[j]:
        b = True
        break
    else:
        b = False
if b:
    print("Число есть в массиве")
else:
    print("Числа нет в массиве")