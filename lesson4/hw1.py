# homework lesson: 4, task 1
"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def sal_calculation(hours: int, per_hour: int, premium: int) -> int:
    """
    Функция для расчета заработной платы.
    :param hours: int
    :param per_hour: int
    :param premium: int
    :return: int
    """
    salary = (hours * per_hour) + premium
    return salary


print(sal_calculation(int(argv[1]), int(argv[2]), int(argv[3])))
