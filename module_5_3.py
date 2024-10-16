class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # название здания
        self.number_of_floors = number_of_floors  # число этажей

    def go_to(self, new_floor):
        if (new_floor > self.number_of_floors) or (new_floor < 1):
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        out = f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
        return out

    def __eq__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return print('ошибка')


    def __lt__(self, other):

        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return print('ошибка')



    def __le__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return print('ошибка')

    def __gt__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return print('ошибка')


    def __ge__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return print('ошибка')

    def __ne__(self, other):
        if isinstance(self, House) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return print('ошибка')


    def __add__(self, value: int):

        if isinstance(value, int) and isinstance(self, House):
            self.number_of_floors = self.number_of_floors + value
            return self
        else:
            return print('ошибка')



    def __radd__(self, value: int):
        return self + value

    def __iadd__(self, value: int):
        new_house = House(self.name, self.number_of_floors)

        return new_house + value


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)



print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)
#
h2 = 10 + h2  # __radd__
print(h2)
#
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__


