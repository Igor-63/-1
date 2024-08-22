

first = int(input("Введите первое целое число "))
second =int(input('Введите второе целое число '))
thirt = int(input("Введите третье целое число "))

if first==second==thirt:
    print (3, 'числа равны')
elif (first==second or  first==thirt or second==thirt):
    print(2, 'числа равны')
else:
    print(0, 'одинаковых чисел нет')



