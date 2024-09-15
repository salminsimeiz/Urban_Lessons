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

    def __is_valid_color(self, r, g, b):
        if r in list(range(256)) and g in list(range(256)) and b in list(range(256)):
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


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
        finally:
            return (f"Треугольник со сторонами {self.__sides[0]}, {self.__sides[1]},"
                    f" {self.__sides[2]} не существует")


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *([sides[0]] * self.sides_count))

    def get_volume(self):
        edge_length = self.get_sides()[0]
        return edge_length ** 3


t1 = Triangle((122, 123, 124), 1, 1, 4)
print(t1.get_square())
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())