
def get_matrix(n=1, m=1, value=0):
    matrix = list()
    matrix_n = list()
    for i in range(0, n):
        matrix_n.clear()
        for j in range(0, m):
            matrix_n.append(value)
        matrix.append(matrix_n)

    if n<1 or m<1:      # если число строк или столбцов меньше единицы
        matrix.clear()  # возвращается пустой список

    return matrix

result1 = get_matrix(-1, 2, 10) #  для значений  n< 1  или  m<1
result2 = get_matrix(3, -1, 42) #  возвращается пустой список

result3 = get_matrix(2, 2, 10)
result4 = get_matrix(3, 5, 42)
result5 = get_matrix(4, 2, 13)

print(result1)
print(result2)

print(result3)
print(result4)
print(result5)






