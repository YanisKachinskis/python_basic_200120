# homework lesson: 3, task 5
"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""


def sum_numbers(numbers: str) -> int:
    """
     Функция считает сумму чисел.
     :param numbers: str
     :return: int
    """
    result = 0
    num_list = [int(item) for item in (users_input.split(' ')) if item.isdigit()]
    result += sum(num_list)
    return result


result = 0
for_exit = ''
while for_exit != 'q':
    users_input = input('Введите несколько чисел через пробел.\nДля выхода из программы введите "q":\n').strip()
    if users_input == 'q':
        for_exit = 'q'
        print(f'Вы вышли из программы. Общая сумма введенных чисел равна {result}.')
        continue
    elif users_input[-1] != 'q':
        result += sum_numbers(users_input)
    else:
        result += sum_numbers(users_input)
        for_exit = 'q'
        print(f'Вы вышли из программы. Общая сумма введенных чисел равна {result}.')
