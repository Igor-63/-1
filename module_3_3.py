def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(3.9, 'машина', )
print_params(4, 'дом', False)

print_params(b=25)  # работает
print_params(c=[1, 2, 3])  # работает

values_list = (8, 'монета', False)
values_dict = {'a': 6, 'b': 'True', 'c': 'yggyg'}

print_params(*values_list)

print_params(values_dict)
print_params(*values_dict)
print_params(**values_dict)

