def invert_dict(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    return inverted_dict


book = {}

while True:
    name = input("Введите ФИО или 'q' для завершения: ")

    if name == 'q':
        break

    phone = input("Введите номер телефона: ")
    book[name] = phone

if book:
    inverted_book = invert_dict(book)
    print("Инвертированный словарь:")
    print(inverted_book)
else:
    print("Словарь пуст.")