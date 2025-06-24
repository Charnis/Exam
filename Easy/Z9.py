N = int(input("N = "))
pro = 1
for i in range(1,N+1):
    pro *= i
print(f"Факториал числа N({N}) = {pro}")