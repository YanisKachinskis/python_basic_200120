# homework lesson: 6, task 5
"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def __init__(self, color, title):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f'Отрисовываем ручкой цвета: {self.color}')


class Pencil(Stationery):

    def __init__(self, color, title):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f'Отрисовываем карандашом цвета: {self.color}')


class Handle(Stationery):

    def __init__(self, color, title):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f'Отрисовываем маркером цвета: {self.color}')


pen = Pen('красный', 'карандаш мягкий')
print(pen.title, pen.color)
pen.draw()
print("-" * 100)

pencil = Pencil('синий', 'ручка шариковая')
print(pencil.title, pencil.color)
pencil.draw()
print("-" * 100)

handle = Handle('оранжевый', 'маркер перманентный')
print(handle.title, handle.color)
handle.draw()
print("-" * 100)