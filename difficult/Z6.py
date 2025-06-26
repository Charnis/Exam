m = [
[1,2,3],
[4,5,6],
[7,8,9]
]
a = 0
print(len(m))
for i in range(len(m)):
    for j in range(len(m)):
        a += m[i][j]
print(a)