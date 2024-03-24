N = int(input("Введите число: "))

if N:
    print("Плохо")
elif N >= 2 and N <= 5:
    print("Неплохо")
elif N >= 6 and N <= 20:
    print("Так себе")
else:
    print("Отлично")