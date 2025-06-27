def is_rotation(s1, s2):
    if len(s1) != len(s2) or not s1:
        return False
    combined = s1 + s1
    return s2 in combined


s1 = input("Введите слов: ")
s2 = input("Введите вращеное слово: ")
print(is_rotation(s1, s2))
