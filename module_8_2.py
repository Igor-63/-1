

def personal_sum(numbers):
        reslt1 = 0
        incorrect_data =0
        for num in numbers:
                try:
                    reslt1 = reslt1 + num
                except TypeError:
                    incorrect_data = incorrect_data+1
                    print(f'В numbers записан некорректный тип данных для подсчета суммы-{num}' )


        return  (reslt1, incorrect_data)



def calculate_average(numbers):
    try:
        rez2 = personal_sum(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

    try:
        count1 = len (numbers) - rez2[1]
        return rez2[0]/count1
    except ZeroDivisionError:
        return 0







print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать







