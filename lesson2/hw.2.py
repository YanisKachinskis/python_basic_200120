number_items = int(input('Введите количество элементов списка:\n'))
my_list = []

for i in range(number_items):
    my_list.append(input(f'Введите {i + 1} элемент списка:\n'))
print(f'Список до изменений: {my_list}')

i = 0
if len(my_list) % 2 == 0:
    while i < len(my_list):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
else:
    while i < (len(my_list) - 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
print(f'Список после изменений: {my_list}')
