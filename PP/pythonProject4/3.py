elements = tuple(map(int, input("Введите числа через пробел: ").split()))
sorted_elements = sorted(elements, key=lambda x: abs(x))
print(sorted_elements)