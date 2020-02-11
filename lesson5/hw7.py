# homework lesson: 5, task 7
"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

i = 0
profit = 0
result = {}
average = {}
with open('7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm_type, proceeds, outlay = line.split(" ")
        if int(proceeds) > int(outlay):
            result[name] = int(proceeds) - int(outlay)
            profit += int(proceeds) - int(outlay)
            i += 1
        else:
            result[name] = int(proceeds) - int(outlay)
average['average_profit'] = profit / i
result = [result, average]

with open('7.json', 'w') as file:
    json.dump(result, file)
