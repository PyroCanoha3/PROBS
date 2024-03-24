text = input("Введите строку: ")
words = text.split()
for i in range(len(words)-2):
    if words[i].isalpha() and words[i+1].isalpha() and words[i+2].isalpha():
        print(True)
        break
else:
    print(False)