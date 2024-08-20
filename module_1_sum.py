
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #оценки
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}    #имена

list_students = list(students) #список студентов
list_students.sort()    # сортировка по алфавиту


grades[0]=sum(grades[0])/len(grades[0]) # средняя оценка
grades[1]=sum(grades[1])/len(grades[1])
grades[2]=sum(grades[2])/len(grades[2])
grades[3]=sum(grades[3])/len(grades[3])
grades[4]=sum(grades[4])/len(grades[4])

stud_dict = {list_students[0]:grades[0], # искомый словарь
             list_students[1]:grades[1],
             list_students[2]:grades[2],
             list_students[3]:grades[3],
             list_students[4]:grades[4]}

print(stud_dict)

