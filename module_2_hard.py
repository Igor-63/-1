# 3 =

random_digit = int(input('введите значение от 2 до 20 '))

while random_digit < 2:
    print('недопустимо, введите снова')
    random_digit = int(input())
numbers = list()
numbers2 = list()
numbers3 = list()
numbers4 = list()

dics1 = {0, ()}

for i in range(1, random_digit):
    numbers.append(i)

digit_len = len(numbers)
i = 0
j = 0

while i < (digit_len - 1):
    j = i
    while j < (digit_len - 1):
        test1 = (numbers[i] + numbers[j + 1]) % random_digit
        test2 = random_digit % (numbers[i] + numbers[j + 1])
        if test1 < 1:
            numbers2.append(int(str(numbers[i]) + str(numbers[j + 1])))
        elif test2 < 1:
            numbers2.append(int(str(numbers[i]) + str(numbers[j + 1])))
        j = j + 1
    i = i + 1

out_code = str()
for i in numbers2:
    out_code = out_code + str(i)
#
# print(numbers)
print('искомый пароль:', out_code)


