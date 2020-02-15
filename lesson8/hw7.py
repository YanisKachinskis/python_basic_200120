# homework lesson: 8, task 7
"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"z={str(self.x)}+{str(self.y)}i" if self.y > 0 else f"z={str(self.x)}{str(self.y)}i"

    def __add__(self, other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return f"z={str(sum_x)}+{str(sum_y)}i" if sum_y > 0 else f"z={str(sum_x)}{str(sum_y)}i"

    def __mul__(self, other):
        mul_x = self.x * other.x - self.y * other.y
        mul_y = self.x * other.y + self.y * other.x
        return f"z={str(mul_x)}+{str(mul_y)}i" if mul_y > 0 else f"z={str(mul_x)}{str(mul_y)}i"


z1 = ComplexNumber(-2, -5)
z2 = ComplexNumber(3, 9)
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)