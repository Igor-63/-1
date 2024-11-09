# Создайте 3 класса (2 из которых будут исключениями):
# Класс Car должен обладать следующими свойствами:
# Атрибут объекта model - название автомобиля (строка).
# Атрибут объекта __vin - self номер автомобиля (целое число). Уровень доступа private.
# Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение.
# Уровень доступа private.
# Атрибут __numbers - номера автомобиля (строка).
# Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.


class Car:
    def __init__(self, model, numbers, vin_number ):
        self.model = model
        self.__numbers =self.__is_valid_numbers(numbers)
        self.__vin = self.__is_valid_vin(vin_number)


    def __is_valid_vin(self, vin_number):

        if not isinstance(vin_number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(vin_number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


    def __is_valid_numbers(self,vin_numbers):

        if not isinstance(vin_numbers, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if vin_numbers > 9999999 or vin_numbers<1000000:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True


class IncorrectVinNumber(Exception):
     def __init__(self, message):
         self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')











