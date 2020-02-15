# homework lesson: 8, task 2
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class DivisionByZeroError(Exception):
    def __init__(self, text='Делить на 0 нельзя!'):
        self.text = text

    def __str__(self):
        return self.text


try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise DivisionByZeroError()
except ValueError:
    print("Вы ввели не число.")
except DivisionByZeroError as err:
    print(err)
else:
    print(f"Результат деления: {a / b}.")
