# homework lesson: 3, task 2
"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user_info(**kwargs):
    """
    Функция выводит информацию о пользователе.
    :param kwargs:
    """
    print(kwargs)


user_info(name="Pavel", surname="Pupkin", year=1984, city="Moscow", mail="P.Pupkin@gmail.com", phone="89213453312")