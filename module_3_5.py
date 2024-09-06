def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))

    #    else:
    #       return first

    # нечеткая постановка задачи.
    # из примера результата следует, что нули не учитываются,
    # при этом, если  нуль последний, то в этом варианте будет умножение на нуль и результат будет равен нулю

    else:
        if number != 0:
            return first
        else:
            return 1


# вариант с учетом исключения последнего нуля. Умножаются только цифры больше нуля


result = get_multiplied_digits(4020340)
print(result)
