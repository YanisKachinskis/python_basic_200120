# homework lesson: 5, task 4
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
"""
file1 = open('4.txt', 'r', encoding='utf-8')
file2 = open('4_new.txt', 'a', encoding='utf-8')
i = 0
rus_numbers = ['Один', 'Два', 'Три', 'Четыре']
for line in file1:
    line = line.replace(line.split(' ')[0], rus_numbers[i])
    i += 1
    file2.write(line)
file1.close()
file2.close()