text = input("Введите строку: ")
words = text.split(",")
result = ""
for word in words:
    if "right" in word:
        word = word.replace("right", "left")
    result += word + ","
print(result[:-1]) # удаляем последнюю запятую
