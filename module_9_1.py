

def apply_all_func(int_list, *functions):
    books1 = {}
    try:
        for function1 in functions:
            books1[function1.__name__] = function1(int_list)
    except TypeError:
         print ('Ошибка. Передано не число')

    return books1



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
