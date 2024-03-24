def int_to_roman(num):
    roman_numerals = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    result = ""

    for value, numeral in roman_numerals.items():
        while num >= value:
            result += numeral
            num -= value

    return result


x = input("Введите целое число от 1 до 3999: ")

try:
    x = int(x)
    if x < 1 or x > 3999:
        raise ValueError
except ValueError:
    print("Неверный ввод. Пожалуйста, введите целое число от 1 до 3999.")
else:
    roman_numeral = int_to_roman(x)
    print("Результат:", roman_numeral)