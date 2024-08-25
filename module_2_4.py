numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # может быть любой набор целых чисел
primes = []
not_primes = []
is_prime = 0
dividers = 0 # число делителей

for i in range(len(numbers)):
    if numbers[i] < 2:          # исключение единицы
        continue
    dividers = 0
    is_prime = numbers[i]
    for j in range(1, is_prime + 1):
        if numbers[i] % j == 0:
            dividers = dividers + 1
    if dividers < 3:             # только 2 делителя
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print('простые числа', primes)
print('больше 2 делителей', not_primes)
