elements = input("Введите элементы массива через пробел: ").split()
# Преобразуем элементы в числа
elements = [float(i) for i in elements]
# Если список пуст, то результат равен 0
if len(elements) == 0:
    result = 0
else:
    # Находим максимум и минимум в списке
    maximum = max(elements)
    minimum = min(elements)
    # Находим разницу между максимумом и минимумом с точностью до третьего знака
    result = round(maximum - minimum, 3)
print("Разница между максимумом и минимумом:", result)
