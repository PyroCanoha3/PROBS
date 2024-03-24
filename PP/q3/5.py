text = input("Введите строку: ")

words = text.split()

for i in range(len(words)-2):
    if words[i].isalpha() and words[i+1].isalpha() and words[i+2].isalpha():
        print("В строке есть три слова подряд")
        break