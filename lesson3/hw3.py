# homework lesson: 3, task 3
"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(num_1: int, num_2: int, num_3: int) -> int:
    """
    Функция считает сумму двух наибольших чисел из трех.
    :param num_1: int
    :param num_2: int
    :param num_3: int
    :return: int
    """
    my_list = [num_1, num_2, num_3]
    result = sorted(my_list, reverse=True)
    return result[0] + result[1]


print(my_func(-16, 45, -15))
