# homework lesson: 4, task 7
"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from math import factorial
from functools import reduce

# Через math.factorial()
def fibo_gen1():
    """
    Функция - генератор - производит подсчет от 1! до 15!.
    :return: int
    """
    for number in range(1, 16):
        result = factorial(number)
        yield result

# Через functools.reduce()
def fibo_gen2():
    """
    Функция - генератор - производит подсчет от 1! до 15!.
    :return: int
    """
    for number in range(1, 16):
        yield reduce(lambda x, y: x * y, [itm + 1 for itm in range(0, number)])


for el in fibo_gen1():
    print(el)

for el in fibo_gen2():
    print(el)
