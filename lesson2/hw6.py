print('Форма ввода данных о товарах в магазине.\n')
number = int(input('Сколько позиций товара нужно ввести?\n'))
i = 1
goods = []
while i <= number:
    name = input(f'Введите название {i} товара:\n')
    price = int(input(f'Введите стоимость {i} товара:\n'))
    quantity = int(input(f'Введите колличественный показатель {i} товара:\n'))
    unit = input(f'Введите единицы измерения для {i} товара:\n')
    goods.append((i, {'название': name, 'цена': price, 'количество': quantity, 'ед': unit}))
    i += 1
print(goods)

names = []
prices = []
quantities = []
units = []
for good in goods:
    names.append(good[1].get('название'))
    prices.append(good[1].get('цена'))
    quantities.append(good[1].get('количество'))
    if good[1].get('ед') in units:
        pass
    else:
        units.append(good[1].get('ед'))
analytics = {'название': names, 'цена': prices, 'количество': quantities, 'ед': units}
print(analytics)
