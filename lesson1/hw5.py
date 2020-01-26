income = int(input('Введите вашу прибыль: '))
outgoing = int(input('Введите ваши издержки: '))
if income > outgoing:
    print('Фирма рабает в прибыль.')
else:
    print('Фирма работает в убыток.')
efficiency = (income / outgoing) * 100
print(f'Ретабельность составляет {round(efficiency, 2)}%.')
employees_num = int(input('Ввведите количество сотрудников фирмы:'))
to_employee = income / employees_num
print(f'Прибыль в рассчете на одного сотрудника: {round(to_employee, 2)}')