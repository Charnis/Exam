year = int(input("Введите год: "))
if year % 4 == 0:
    print(f"{year}-й год високосный")
else:
    print(f"{year}-й год не високосный")