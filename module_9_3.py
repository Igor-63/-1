first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']





first_result = (abs (len (str1[0]) - len (str1[1]))
                for str1 in zip(first, second)
                if abs (len (str1[0]) - len (str1[1])))


second_result = ((len(first[str]) == (len(second[str]))
                       for str in range(len(first))))



print(list(first_result))
print(list(second_result))