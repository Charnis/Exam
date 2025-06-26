m = [
[1,2,3],
[4,10,6],
[7,8,9]
]
g = []
print(len(m))
for i in range(len(m)):
    for j in range(len(m)):
        g.append(m[i][j])
        a = max(g)
print(a)