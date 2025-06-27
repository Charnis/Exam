def caesar_cipher(text, shifts, alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'):
    result = []
    for char in text.lower():
        if char in alphabet:
            index = (alphabet.index(char) + shifts) % len(alphabet)
            result.append(alphabet[index])
        else:
            result.append(char)
    return ''.join(result)

message = input()
shifts = int(input())
encrypted = caesar_cipher(message, shifts)
decrypted = caesar_cipher(encrypted, -shifts)

print(f"Исходное: {message}")
print(f"Зашифрованное (сдвиг +{shifts}): {encrypted}")
print(f"Расшифрованное (сдвиг -{shifts}): {decrypted}")