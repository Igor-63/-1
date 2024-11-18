
def is_prime(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)

        del_digit = 0

        for i in range(1, original_result + 1):
            if (original_result % i):
                pass
            else:
                del_digit = del_digit + 1

        if del_digit > 2:
            print('Составное')
        else:
            print('Простое')
        return original_result

    return wrapper




@is_prime

def sum_three (one_digit, two_digit, three_two_digit ):
    return (one_digit + two_digit + three_two_digit)


result = sum_three(2, 3, 6)

print(result)




