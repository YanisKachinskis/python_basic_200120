# homework lesson: 6, task 4
"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self):
        self.speed = 0
        self.color = None
        self.name = None
        self.is_police = False

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction: str):
        print(f'Машина повернула {direction}.')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}.')


class TownCar(Car):
    def __init__(self, speed: int, color, name, is_police=False):
        super().__init__()
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость автомобиля {self.speed}. Вы привышаете на {self.speed - 60} км/ч.')
        else:
            print(f'Текущая скорость автомобиля {self.speed}.')


class SportCar(Car):
    def __init__(self, speed: int, color, name, is_police=False):
        super().__init__()
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police


class WorkCar(Car):
    def __init__(self, speed: int, color, name, is_police=False):
        super().__init__()
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость автомобиля {self.speed}. Вы привышаете на {self.speed - 40} км/ч.')
        else:
            print(f'Текущая скорость автомобиля {self.speed}.')

class PoliceCar(Car):
    def __init__(self, speed: int, color, name, is_police=True):
        super().__init__()
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police


car_1 = TownCar(70, 'зеленый', 'Mini Cooper')
print(car_1.speed, car_1.color, car_1.name, car_1.is_police)
car_1.go()
car_1.turn('налево')
car_1.stop()
car_1.show_speed()
print('#' * 100)

car_2 = SportCar(200, 'красный', 'Ferrari F50')
print(car_2.speed, car_2.color, car_2.name, car_2.is_police)
car_2.go()
car_2.turn('направо')
car_2.stop()
car_2.show_speed()
print('#' * 100)

car_3 = WorkCar(45, 'черный', 'School bus')
print(car_3.speed, car_3.color, car_3.name, car_3.is_police)
car_3.go()
car_3.turn('налево')
car_3.stop()
car_3.show_speed()
print('#' * 100)

car_4 = PoliceCar(150, 'черно-белый', 'Ford Mustang')
print(car_4.speed, car_4.color, car_4.name, car_4.is_police)
car_4.go()
car_4.turn('направо')
car_4.stop()
car_4.show_speed()
print('#' * 100)
