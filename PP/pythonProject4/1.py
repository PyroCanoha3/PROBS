elements = list(map(int, input("Введите числа через пробел: ").split()))
sum = 0
for i in range(0, len(elements), 2):
    sum += elements[i]
if len(elements) > 0:
    result = sum * elements[-1]
else:
    result = 0
print(result)