num = int(input("Введите целое число: "))
inverted_num = 0

while num > 0:
    last_digit = num % 10 # получаем последнюю цифру числа
    inverted_num = inverted_num * 10 + last_digit # добавляем последнюю цифру в начало инвертированного числа
    num //= 10 # удаляем последнюю цифру из исходного числа

print("Инвертированное число:", inverted_num)
