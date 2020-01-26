seconds = int(input('Введите время в секундах: '))
minutes = seconds // 60
seconds_left = seconds % 60
hours = minutes // 60
minutes_left = minutes % 60
print(f'{hours:02}:{minutes_left:02}:{seconds_left:02}')
