dates = []
rates = []

while True:
    date = input("Введите дату или 'q' для завершения: ")

    if date == 'q':
        break

    rate = float(input("Введите курс валюты: "))

    dates.append(date)
    rates.append(rate)

if dates and rates:
    currency_dict = dict(zip(dates, rates))
    print("Словарь с курсами валют:")
    print(currency_dict)
else:
    print("Списки пусты.")