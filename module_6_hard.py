import math


class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides):

        self.__sides = []

        if self.sides_count != len(sides):
            self.__sides = [1] * self.sides_count

        self.set_sides(*sides)

        self.set_color(*color)

        self.sides_count = len(self.__sides)

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if isinstance((r + g + b), int):
            if r < 0 or r > 255:
                print(f'ошибка красного цвета {r}')
                return False
            elif g < 0 or g > 255:
                print(f'ошибка зеленого цвета {g}')
                return False
            elif b < 0 or b > 255:
                print(f'ошибка синего цвета {b}')
                return False
            else:
                return True
        else:
            print('Ошибка. Дробное значение цвета  ')
            return False

    def __len__(self):
        perimetr = 0
        for side in self.__sides:
            perimetr = perimetr + side
        return perimetr

    def set_color(self, r, g, b):

        if self.__is_valid_color(r, g, b):
            self.__color = []
            self.__color = r, g, b

    def is_valid_sides(self, sides):
        if self.sides_count == 0:
            for side1 in sides:
                if side1 < 0 or not isinstance(side1, int):
                    return False
        else:
            if len(sides) != len(sides):
                return False

        for side1 in sides:
            if side1 < 0 or not isinstance(side1, int):
                return False
            return True

    def set_sides(self, *new_sides):

        if self.is_valid_sides(new_sides):
            if self.sides_count == len(new_sides):
                self.__sides = list(new_sides)

    def get_sides(self):
        return list(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list, *sides):
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()
        self.__radius = self.__radius[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list, *sides):
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()
        self.__radius = self.__radius[0] / (2 * math.pi)

    def get_square(self):
        half_perimetr = len(self) / 2

        a, b, c = self.get_sides()

        return math.sqrt(half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list, *sides):
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = new_sides * 12
            super().set_sides(*new_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
