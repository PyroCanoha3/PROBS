text = input("Введите кусок текста: ")
result = ""
for char in text:
    if char.isupper():
        result += char
print(result)