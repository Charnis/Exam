m = [9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(len(m)-1):
    for j in range(len(m) - i - 1):
        if m[j] > m[j+1]:
            m[j], m[j+1] = m[j+1], m[j]
print(m)