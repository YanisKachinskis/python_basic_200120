# homework lesson: 5, task 2
"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
i = 1
with open('3.txt', 'r', encoding='utf-8') as file:
    all_data = file.readlines()
    print(f"В файле {len(all_data)} строк(и)")
    for line in all_data:
        print(f"В {i} строке - {len(line.split(' '))} слов(о/а)")
        i += 1
