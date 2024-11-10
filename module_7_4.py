team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / tasks_total, 2)
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# Использование %:
# Переменные: количество участников первой команды (team1_num)
print('В команде Мастера кода участников: %s !' % team1_num)
# Переменные: количество участников в обеих командах (team1_num, team2_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print()

# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
# Переменные: время за которое команда 2 решила задачи (team1_time).
print('Волшебники данных решили задачи за {} с !'.format(team1_time))
print()

# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
print(f'Команды решили {score_1} и {score_2} задач.')
# Переменные: исход соревнования (challenge_result).
print(f'Результат битвы: {challenge_result}')
# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
