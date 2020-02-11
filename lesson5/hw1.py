# homework lesson: 5, task 1
"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('my_file.txt', 'w', encoding='utf-8') as file:
    i = 1
    lines = []
    line = None
    while line != '':
        line = input(f'Введите {i} строку:\n')
        i += 1
        lines.append(line + '\n')
    file.writelines(lines)

