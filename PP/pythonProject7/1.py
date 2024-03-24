text = input("Введите текст: ")

# Удаление знаков препинания и приведение текста к нижнему регистру
text = text.lower()
text = text.replace(",", "").replace(".", "").replace("!", "").replace("?", "")

# Разделение текста на слова
words = text.split()

# Создание словаря популярности слов
words_popularity = {}
for word in words:
    if word in words_popularity:
        words_popularity[word] += 1
    else:
        words_popularity[word] = 1

# Создание словаря популярности букв
chars_popularity = {}
for word in words:
    for char in word:
        if char in chars_popularity:
            chars_popularity[char] += 1
        else:
            chars_popularity[char] = 1

print("Словарь популярности слов:", words_popularity)
print("Словарь популярности букв:", chars_popularity)
