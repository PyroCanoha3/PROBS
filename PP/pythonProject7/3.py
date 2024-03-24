def find_best_exchange_rate(rates):
    best_bank = None
    best_rate = None

    for bank, rate in rates.items():
        if best_rate is None or rate < best_rate:
            best_bank = bank
            best_rate = rate

    return best_bank, best_rate


rates = {}

while True:
    bank = input("Введите название банка или 'q' для завершения: ")

    if bank == 'q':
        break

    try:
        rate = float(input("Введите курс покупки доллара: "))
        rates[bank] = rate
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")

if rates:
    best_bank, best_rate = find_best_exchange_rate(rates)
    print("Наиболее привлекательное предложение:")
    print(best_bank, "->", best_rate)
else:
    print("Нет данных о курсах валюты.")