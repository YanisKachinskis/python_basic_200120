# homework lesson: 3, task 4
"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


# решение с помощью **
def my_func_1(x: float, y: int) -> float:
    """
    Функция возводит число x в степень y.
    :param x: int
    :param y: int
    :return: float
    """
    return x ** y


# решение с помощью цикла
def my_func_2(x: float, y: int) -> float:
    """
    Функция возводит число x в степень y.
    :param x: int
    :param y: int
    :return: float
    """
    i = 0   #счетчик
    result = 1
    while i < abs(y):
        result *= x
        i += 1
    return 1 / result


print(my_func_1(0.4, -2))
print(my_func_2(0.4, -2))
