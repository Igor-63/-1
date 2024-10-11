class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, new_owner, model, color, engine_power):
        self.owner = new_owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power

    def get_model(self):
        mod = self.__model
        print(f'Модель: {mod}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print( f'Владелец: {self.owner}')

    def set_color(self, newcolor):
        not_change_color = True
        for i in Vehicle.__COLOR_VARIANTS:
            if i.lower() == newcolor.lower():
                self.__color = newcolor
                not_change_color = False
        if not_change_color:
            print(f'Нельзя сменить цвет на {newcolor}')



class Sedan(Vehicle):
    # седан

    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# # Изначальные свойства
vehicle1.print_info()
#
# # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
vehicle1.print_info()
#
