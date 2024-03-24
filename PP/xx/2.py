def get_permutations(x, y, z, n):
    permutations = []

    # Перебираем все возможные значения x, y и z
    for i in [x, y, z]:
        for j in [x, y, z]:
            for k in [x, y, z]:
                # Проверяем условие x + y - z > n
                if i + j - k > n:
                    permutation = [i, j, k]
                    permutations.append(permutation)

    return permutations


# Ввод данных
x = int(input("Введите значение x: "))
y = int(input("Введите значение y: "))
z = int(input("Введите значение z: "))
n = int(input("Введите значение n: "))

# Получение списка перестановок
result = get_permutations(x, y, z, n)

# Вывод результата
print("Список перестановок:", result)
