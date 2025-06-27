words = ["code", "edoc", "da", "d", "asd", "agd"]

for i in words:
    for j in words:
        s = i + j
        if s == s[::-1]:
            print(f"{i} + {j} = {s} (палиндром)")