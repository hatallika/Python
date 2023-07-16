# Домашнее задание#
# Реализация работы с классами, наследованием и перегрузкой методами
#
# Планируемый результат:#
# Корректно реализован класс, использующий псевдо частные методы и реализующий перегрузку методов
import math


# Определим класс Фигуры и унаследуем Круг, Квадрат, Треугольник переопределяя методы поиска периметра и площади
# Входные параметры будем менять от типа фигуры
# Перегрузим метод __str__
class Shapes:
    PI = math.pi

    def __str__(self):
        return f"Класс {self.__class__.__name__}, наследуемый из {self.__class__.__bases__} "

    def __init__(self, *args):
        self.sides = args

    def get_perimeter(self):
        if len(self.sides) > 1:
            return sum(self.sides)
        else:
            print('It is circle')
            return False

    def get_square(self):
        pass

    @property
    def show_pi(self):
        print(self.PI)


class Circle(Shapes):

    def __init__(self, circle_len):
        super().__init__(circle_len)

        print(f'Задана окружность с длинной {circle_len}')
        # self._radius = circle_len / (2 * self.PI)

    # переопределим поиск площади для окружности
    def get_square(self):
        return self.PI * self.__get_radius() ** 2

    def __get_radius(self):
        print('Сработал частный метод поиск радиуса')
        return self.sides[0] / (2 * self.PI)


class Square(Shapes):
    def __init__(self, side):
        super().__init__(side)
        print(f'Задан квадрат со сторонами {side}')

    def get_square(self):
        return self.sides[0] * self.sides[0]

    def get_perimeter(self):
        return self.sides[0] + self.sides[0]


class Triangle(Shapes):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)
        print(f'Задан треугольник со сторонами {side1}, {side2}, {side3}')

    def get_square(self):
        p = sum(self.sides) / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5


c = Circle(5)
print('Площадь окружности', c.get_square())

sq = Square(2)
print('Периметр квадрата', sq.get_perimeter())
print('Площадь квадрата', sq.get_square())

t = Triangle(5, 5, 6)
print('Периметр треугольника', t.get_perimeter())
print('Площадь треугольника', t.get_square())

# Перегрузка метода __str__
print(c)
print(sq)
print(t)
# Вызов без скобок
t.show_pi
# f = Shapes(5, 5, 6)
# print(f.get_square())
