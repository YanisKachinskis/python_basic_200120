# homework lesson: 8, task 1
"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:

    def __init__(self, date: "str в виде 'день-месяц-год'"):
        self.date = date

    @classmethod
    def date_in_number(cls, date):
        day, month, year = (list(map(int, date.split('-'))))
        return day, month, year

    @staticmethod
    def date_check(day, month, year):
        if (0 < day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]) or (0 < day <= 30 and month in [4, 6, 9, 11]) or \
                (0 < day <= 29 and month == 2):
            if 0 < year <= 2020:
                print(f"Дата указана корректно.")
            else:
                print("Указан неверный год.")
        else:
            print("День и(или) месяц указаны неверно.")


input_date = Data.date_in_number('15-11-2020')
print(*input_date)
Data.date_check(*input_date)
