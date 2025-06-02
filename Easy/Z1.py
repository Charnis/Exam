m=[]
n = int(input())
s = 0
for i in range(1, n+1):
    m.append(i)
    s += m[i-1]
print(m,s)