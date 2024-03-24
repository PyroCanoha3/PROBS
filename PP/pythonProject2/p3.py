
num = float(input("Введите число: "))
formatted_num = "{:.2f}".format(num) # округляем до 2 знаков после запятой и преобразуем в строку
padded_num = formatted_num.zfill(11) # дополняем слева нулями до 11 знаков
print("Форматированное число:", padded_num)