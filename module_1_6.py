


my_dict={'Игорь':1963,'Маша':1981}
print()
print('Мой словарь:',my_dict)
print('Ключ есть:',my_dict.get('Игорь'))
print('Ключ отсутствует:',my_dict.get('Игрь'))
my_dict.update({'Витя':1995, 'Света':2001})
print('Добавлены элементы',my_dict)

print('Удален элемент', my_dict.pop('Маша'))
print('Итоговый словарь:',my_dict)

my_set= {1, 'Яблоко', 2.34, 1, 12, 'Яблоко'}

print()

print('Исходное множество',my_set)
my_set.update({178, 'Вишня'})

print('Добавлены элементы',my_set)
my_set.discard(178)
print('Удален элемент',my_set)
