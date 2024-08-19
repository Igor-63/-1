immutable_var=8,"Power", 3.1415926
print(immutable_var)
#immutable_var[0]=10 ошибка. непосредственно изменить элемент кортежа невозможно по определению.
mutable_list =[12, 'выводы', 2.17]
print(mutable_list)
mutable_list[0]=67 # изменять значения элементов списка можно.
print(mutable_list[0])