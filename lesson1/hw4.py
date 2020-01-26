number = int(input('Введите целое положительное число: '))
result = 0
while number > 0:
    if number % 10 > result:
        result = number % 10
    number = number // 10
print(result)
