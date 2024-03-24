num = int(input("Введите целое число: "))
inverted_num = 0
is_negative = False

if num < 0:
    is_negative = True
    num = abs(num)

while num > 0:
    last_digit = num % 10 # получаем последнюю цифру числа
    inverted_num = inverted_num * 10 + last_digit # добавляем последнюю цифру в начало инвертированного числа
    num //= 10 # удаляем последнюю цифру из исходного числа

if is_negative:
    inverted_num = -inverted_num

if abs(inverted_num) > 2**31-1:
    print(0)
else:
    print("Инвертированное число:", inverted_num)