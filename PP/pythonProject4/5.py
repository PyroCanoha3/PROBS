text = input("Введите текст: ")
vowels = "AEIOUY"
consonants = "BCDFGHJKLMNPQRSTVWXZ"
count = 0
words = text.split()
for word in words:
    if len(word) > 1:
        for i in range(len(word)-1):
            if (word[i].upper() in vowels and word[i+1].upper() in consonants) or (word[i].upper() in consonants and word[i+1].upper() in vowels):
                continue
            else:
                break
        else:
            count += 1
print("Количество полосатых слов в тексте:", count)


