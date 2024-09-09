from math import pi
from math import sqrt


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if r in list(range(256)) and g in list(range(256)) and b in list(range(256)):
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for item in sides:
                if item > 0:
                    return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], int) and new_sides[0] > 0:
            super().set_sides(*new_sides)
            self.__radius = new_sides[0] / (2 * pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__sides = sides

    def get_square(self):
        try:
            a, b, c = self.__sides
            s = (a + b + c) / 2
            return sqrt(s * (s - a) * (s - b) * (s - c))
        except:
            return (f"Треугольник со сторонами {self.__sides[0]}, {self.__sides[1]},"
                    f" {self.__sides[2]} не существует")


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        self.__sides = sides

    def set_sides(self, *sides):
        if len(sides) == 1 and isinstance(sides[0], int) and sides[0] > 0:
            side_length = sides[0]
            self.__sides = [side_length] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3


c1 = Circle((0, 0, 0), 10)
c1.set_color(100, 23, 77)
print(c1.get_color())
c1.set_sides(15)
print(c1.get_sides())
print(len(c1))
print(c1.get_square())
t1 = Triangle((122, 123, 124), 1, 1, 4)
print(t1.get_square())
cube1 = Cube((222, 35, 130), 6)
cube1.set_color(11, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
cube1 = Cube((222, 35, 130), 4)
print(cube1.get_volume())
