def get_doubled_odd_numbers(n):
    numbers = []

    # Перебираем все числа от 0 до n
    for i in range(n + 1):
        # Проверяем, является ли число нечетным
        if i % 2 != 0:
            # Если число нечетное, добавляем его удвоенное значение в список
            numbers.append(i * 2)

    return numbers


# Ввод данных
n = int(input("Введите значение n: "))

# Получение списка удвоенных нечетных чисел
result = get_doubled_odd_numbers(n)

# Вывод результата
print("Список удвоенных нечетных чисел:", result)
