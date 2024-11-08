# число знаков после запятой, чтобы не выводить лишние знаки

def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0




def add_everything_up(a, b):

    rez1 = 0

    try:
        rez1 = round((a+b), max(get_count(a), get_count(b) ))
    except TypeError:
        rez1 = str(a) + str(b)
    finally:
        return rez1



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))




