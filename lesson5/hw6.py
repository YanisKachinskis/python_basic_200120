# homework lesson: 5, task 6
"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""
classes_dict = {}
with open('6.txt', 'r', encoding='utf-8') as file:
    classes = file.readlines()
    for itm in classes:
        try:
            lectures = int(itm.split()[1].rstrip('(л)'))
        except ValueError as e:
            lectures = 0
        try:
            practice = int(itm.split()[2].rstrip('(пр)'))
        except ValueError as e:
            practice = 0
        try:
            labs = int(itm.split()[3].rstrip('(лаб)'))
        except ValueError as e:
            labs = 0
        classes_dict[itm.split(" ")[0].rstrip(':')] = lectures + practice + labs
    print(classes_dict)
