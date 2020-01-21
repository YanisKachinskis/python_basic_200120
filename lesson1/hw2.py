seconds = int(input('Введите время в секундах: '))
minutes = seconds // 60
seconds_left = seconds % 60
hours = minutes // 60
minutes_left = minutes % 60
print(f'{hours}:{minutes_left}:{seconds_left}')
