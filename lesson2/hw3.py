month = input('Введите чиловое значение месяца:\n')

# Решение со списом
month_list = ['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
if month in month_list[:3]:
    print('Данный месяц относится к сезону - зима')
elif month in month_list[3:6]:
    print('Данный месяц относится к сезону - весна')
elif month in month_list[6:9]:
    print('Данный месяц относится к сезону - лето')
elif month in month_list[9:]:
    print('Данный месяц относится к сезону - осень')

# Решение со словарем
month_dict = {('12', '1', '2'): 'зима', ('3', '4', '5'): 'весна', ('6', '7', '8'): 'лето', ('9', '10', '11'): 'осень'}
for season in month_dict.keys():
    if month in season:
        print(f'Данный месяц относится к сезону - {month_dict.get(season)}')
