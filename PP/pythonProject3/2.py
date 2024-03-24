x = int(input("Введите число: "))
if x % 2 != 0:
    result = "Плохо"
elif x in [2, 5]:
    result = "Неплохо"
elif x in range(6, 21):
    result = "Так себе"
else:
    result = "Отлично"
print(result)