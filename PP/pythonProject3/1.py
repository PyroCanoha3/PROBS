num = int(input("Введите число: "))
if num % 3 == 0 and num % 5 == 0:
    result = "Fizz Buzz"
elif num % 3 == 0:
    result = "Fizz"
elif num % 5 == 0:
    result = "Buzz"
else:
    result = str(num)
print(result)