# homework lesson: 7, task 2
"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1

    @abstractmethod
    def textile_consumption(self):
        pass

    @staticmethod
    def total_count():
        return Coat.total_text_consumption() + Suit.total_text_consumption()


class Coat(Clothes):
    count = 0
    coat_dict = {}

    def __init__(self, size, name):
        super().__init__(name)
        self.size = size
        Coat.count += 1
        self.coat_dict[self.name] = round(self.textile_consumption, 2)

    @property
    def textile_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)

    @staticmethod
    def total_text_consumption():
        textile = 0
        for coat in Coat.coat_dict:
            textile += Coat.coat_dict[coat]
        return Coat.count * textile


class Suit(Clothes):
    count = 0
    suit_dict = {}

    def __init__(self, height, name):
        super().__init__(name)
        self.height = height
        Suit.count += 1
        self.suit_dict[self.name] = round(self.textile_consumption, 2)

    @property
    def textile_consumption(self):
        return round(self.height * 2 + 0.3, 2)

    @staticmethod
    def total_text_consumption():
        textile = 0
        for suit in Suit.suit_dict:
            textile += Suit.suit_dict[suit]
        return round(Suit.count * textile)


coat1 = Coat(46, 'зимнее пальто1')
coat2 = Coat(44, 'зимнее пальто2')

print(coat1.textile_consumption)
print(Coat.total_text_consumption())

suit1 = Suit(175, 'смокинг')
suit2 = Suit(160, 'тройка')
suit3 = Suit(185, 'летний костюм')
print(suit1.textile_consumption)
print(Suit.total_text_consumption())

print(Clothes.total_count())
