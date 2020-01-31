# homework lesson: 4, task 6
"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count, cycle


# Задача а
def num_gen(num: int):
    """
    Функция - бесконечный генератор целых чисел, начиная с аргумента,
    переданного в функцию.
    :param num: int
    """
    for i in count(num):
        print(i)


#num_gen(2)

# Задача б
def cyc(iterable: list):
    """
    Функция принимает итерируемый объект и выводит его значения бесконечно.
    :param iterable: list
    """
    for itm in cycle(iterable):
        print(itm)

#cyc([1, "A", True])
