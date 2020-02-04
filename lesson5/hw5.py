# homework lesson: 5, task 5
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
numbers = ['1', '14', '56', '13', '65', '45', '6']
with open('5.txt', 'w', encoding='utf-8') as file:
    file.write(' '.join(numbers))

summa = 0
with open('5.txt', 'r', encoding='utf-8') as file:
    numbers = file.readline()
    for number in numbers.split(' '):
       summa += int(number)
    print(summa)