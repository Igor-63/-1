
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

result1 = 'В команде Мастера кода участников %s' % team1_num
print (result1)

result1 = 'В команде Волшебники Данных участников %s' % team2_num
print (result1)


result1 = 'Итого сегодня в командах участников: %s и  %s'  % (team1_num, team2_num)

print (result1)




result1 = "Команда Волшебники данных решила задач: {:d}"
result1 = result1.format(score_1)

print (result1)

result1 = "Команда Мастера кода решила задач: {:d}"
result1 = result1.format(score_2)
print (result1)


result1 = "Волшебники данных решили задачи за {:.1f} с "
result1 = result1.format(team1_time)
print (result1)

result1 = "Команда Мастера кода решила  задачи за {:.1f} с "
result1 = result1.format(team2_time)
print (result1)


result1 = f'Команды решили {score_1} и {score_2} задач'
print (result1)


time_avg = (team1_time + team2_time)/(score_1 + score_2)


result1 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!."
print (result1)



if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result1 = 'Победа команды Волшебники Данных!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result1 = 'Победа команды Мастера кода!'
else:
    result1 = 'Ничья!'

print (result1)








