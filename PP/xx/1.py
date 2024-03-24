def get_non_unique_elements(arr):
    count_dict = {}
    non_unique_elements = []

    # Подсчитываем количество каждого элемента в массиве
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Добавляем в новый массив только неуникальные элементы
    for num, count in count_dict.items():
        if count > 1:
            non_unique_elements.append(num)

    return non_unique_elements


# Ввод данных
arr = input("Введите элементы массива, разделенные пробелами: ").split()
arr = [int(num) for num in arr]

# Получение неуникальных элементов
result = get_non_unique_elements(arr)

# Вывод результата
print("Неуникальные элементы:", result)
