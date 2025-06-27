number = int(input("Введите число "))
summ = 0
for i in range(1, number):
    if number % i == 0:
       summ += i
if summ == number:
    print(f"Число {number} является совершенным")
else:
    print(f"Число {number} не является совершенным")
