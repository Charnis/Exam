m = input()
k = m.lower().replace(' ', '')
if k == k[::-1]:
    print(1)
else:
    print(0)
