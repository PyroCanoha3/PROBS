text = input("Введите текст: ")

result = ""

for char in text:
    if char.isupper():
        result += char

print(result)
