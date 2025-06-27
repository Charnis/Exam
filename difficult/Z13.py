s = input()

if not s:
    compressed = s
else:
    compressed = []
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            compressed.append(f"{s[i - 1]}{cnt}")
            cnt = 1
    compressed.append(f"{s[-1]}{cnt}")
    compressed = "".join(compressed)
    if len(compressed) >= len(s):
        compressed = s

print(compressed)