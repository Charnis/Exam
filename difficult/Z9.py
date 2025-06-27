s = 'aabbbAAAABBBBB'
s = sorted(list(s))
print(s)
b = set(s)
print(b)
for i in range(len(s)):
    print(f"{s[i]} = {s.count(s[i])} ")
