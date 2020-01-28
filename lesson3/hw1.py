# homework lesson: 3, task 1
"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(num_1: int, num_2: int) -> float:
    """
    Функция выполняет деление первого числа на второе.
    Возвращает результат деления.

    :param num_1: int
    :param num_2: int
    :return: float
    """
    try:
        return num_1 / num_2
    except ZeroDivisionError as z:
        print('На ноль делить нельзя!')


while True:
    try:
        number_1 = int(input('Введите первое число:\n'))
        number_2 = int(input('Введите второе число:\n'))
        break
    except ValueError as e:
        print('Программа работает только с числами!')
        continue
result = division(number_1, number_2)
if result is None:
    print('Условия задачи были заданы неверно.')
else:
    print(f'Результат вычисления: {result}')
