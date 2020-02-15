# homework lesson: 8, task 4, 5, 6
"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self._id = 0
        self.in_storage = []

    def __str__(self):
        return f"Оборудование {self.name}, модель - {self.model}"

    @abstractmethod
    def get_to_storage(self):
        """
        Метод передачи оборудования на склад.
        """
        self.in_storage.append([self.name, self.model])

    @abstractmethod
    def set_to_department(self):
        """
        Метод передачи оборудования со склада в один из департаментов.
        """
        self.in_storage.remove([self.name, self.model])


class Printer(OfficeEquipment):
    _total_amount = 0
    _storage_amount = 0
    _id = 0
    in_storage = [{}, _storage_amount]

    def __init__(self, name, model, colored: bool):
        super().__init__(name, model)
        self.colored = colored
        Printer._total_amount += 1
        Printer._id += 1
        self._id += Printer._id

    def get_to_storage(self):
        Printer.in_storage[0][self._id] = [self.name, self.model, self.colored]
        Printer._storage_amount += 1
        Printer.in_storage[1] = Printer._storage_amount
        return Printer.in_storage

    def set_to_department(self):
        Printer._storage_amount -= 1
        del Printer.in_storage[0][self._id]
        Printer.in_storage[1] = Printer._storage_amount
        return Printer.in_storage


class Scanner(OfficeEquipment):
    _total_amount = 0
    _storage_amount = 0
    _id = 0
    in_storage = [{}, _storage_amount]

    def __init__(self, name, model, page_format):
        super().__init__(name, model)
        self.page_format = page_format
        Scanner._total_amount += 1
        Scanner._id += 1
        self._id += Scanner._id

    def get_to_storage(self):
        Scanner.in_storage[0][self._id] = [self.name, self.model, self.page_format]
        Scanner._storage_amount += 1
        Scanner.in_storage[1] = Scanner._storage_amount
        return Scanner.in_storage

    def set_to_department(self):
        Scanner._storage_amount -= 1
        del Scanner.in_storage[0][self._id]
        Scanner.in_storage[1] = Scanner._storage_amount
        return Scanner.in_storage


class Copier(OfficeEquipment):
    _total_amount = 0
    _storage_amount = 0
    _id = 0
    in_storage = [{}, _storage_amount]

    def __init__(self, name, model, max_printed_pages):
        super().__init__(name, model)
        self.max_printed_pages = max_printed_pages
        Copier._total_amount += 1
        Copier._id += 1
        self._id += Copier._id

    def get_to_storage(self):
        Copier.in_storage[0][self._id] = [self.name, self.model, self.max_printed_pages]
        Copier._storage_amount += 1
        Copier.in_storage[1] = Copier._storage_amount
        return Copier.in_storage

    def set_to_department(self):
        Copier._storage_amount -= 1
        del Copier.in_storage[0][self._id]
        Copier.in_storage[1] = Copier._storage_amount
        return Copier.in_storage


class InputFormatError(Exception):
    def __init__(self, text='Формат страницы должен соответствовать ISO 216 (буква из латинской раскладки).\n'):
        self.text = text

    def __str__(self):
        return self.text


# работа с экземплярамм класса Printer
a = Printer('Принтер для рабочего места', "Epson X-6", False)
b = Printer('Принтер для фотопечати', "HP BDR-7000", True)
c = Printer('Принтер для начальника', "Lexmark BFG-3000", True)
print(a.get_to_storage)
print(b.get_to_storage)
print(c.get_to_storage)
print(c.set_to_department)
print(a)
# работа с экземплярамм класса Scanner
d = Scanner('Сканнер общего пользования', "Cannon F100", "A4")
e = Scanner('Сканнер для отдела рекламы', "Cannon F3000", "A3")
print(d.get_to_storage())
print(e.get_to_storage())
print(e.set_to_department())
print(d)
# работа с экземплярамм класса Copier
f = Copier('Копир для рекламщиков', "Xerox 5005", 50000)
g = Copier('Копир в приемную директора', "Xerox 500-P", 10000)
print(f.get_to_storage())
print(g.get_to_storage())
print(f.set_to_department())
print(g)

# проверка вводимых пользоваиелем данных на примере атрибута класса Scanner - формат страницы (pages_format)
name = input(f'Введите имя сканера: ')
model = input(f'Введите модель сканера: ')
while True:
    try:
        page_format = input(f'Введите формат страницы для этого сканера(A4, A3 или A2): ')
        if page_format in ['A4', 'A3', 'A2']:
            h = Scanner(name, model, page_format)
            break
        else:
            raise InputFormatError
    except InputFormatError as error:
        print(error)
        continue
print(h)
print(h.get_to_storage())
