elements = input("Введите элементы массива через пробел: ").split()
# Преобразуем элементы в числа
elements = [int(i) for i in elements]
# Сортируем массив
elements.sort()
# Находим середину массива
middle = len(elements) // 2
# Если количество элементов нечетное, то медиана - это элемент посередине
if len(elements) % 2 == 1:
    median = elements[middle]
else:
    # Если количество элементов четное, то медиана - это среднее значение двух элементов посередине
    median = (elements[middle - 1] + elements[middle]) / 2
print("Медиана массива:", median)
