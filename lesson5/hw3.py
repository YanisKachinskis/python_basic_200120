# homework lesson: 5, task 3
"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
info = {}
sum_salary = 0
with open('3.txt', 'r', encoding='utf-8') as file:
    employees = file.readlines()
    for employee in employees:
        name, salary = employee.split(' ')
        info[name] = int(salary)
        if int(salary) < 20000:
            print(f"Сотрудники {name} имеет доход ниже 20000 в месяц.")
        sum_salary += int(salary)
    print(f"Средний доход на сотрудников: {sum_salary/len(employees)}")