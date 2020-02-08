# homework lesson: 6, task 1
"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и
вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
import time
from itertools import cycle


class TrafficLight:
    __color = 'red'

    # без проверки порядка режимов
    def running(self):
        while True:
            self.__color = 'красный'
            print(f"Загорелся {self.__color} сигнал светофора!")
            time.sleep(7)
            self.__color = 'желтый'
            print(f"Загорелся {self.__color} сигнал светофора!")
            time.sleep(2)
            self.__color = 'зеленый'
            print(f"Загорелся {self.__color} сигнал светофора!")
            time.sleep(7)
    # с проверкой порядка работы режимов
    def running1(self):
        for next_color in cycle(['yellow', 'green', 'red']):
            if self.__color == 'red' and next_color == 'yellow':
                print(f"Загорелся {self.__color} сигнал светофора!")
                time.sleep(7)
                self.__color = next_color
            elif self.__color == 'yellow' and next_color == 'green':
                print(f"Загорелся {self.__color} сигнал светофора!")
                time.sleep(2)
                self.__color = next_color
            elif self.__color == 'green' and next_color == 'red':
                print(f"Загорелся {self.__color} сигнал светофора!")
                time.sleep(7)
                self.__color = next_color
            else:
                break
        print("Был нарушен порядок переключения режимов.")


a = TrafficLight()
a.running()
