students_count = int(input('Студентов на курсе: '))
tasks_count = int(input('Заданий: '))
student_names = [input(f'Имя студента {i + 1}: ') for i in range(students_count)]
marks = dict()

# Ввод оценок
for student in student_names:
    print(f'Оценки студента {student}')
    marks[student] = list()
    for task in range(tasks_count):
        mark = -1
        while not(0 < mark < 10):
            mark = int(input(f'{task + 1}: '))
        marks[student].append(mark)

print('Топ 3 по рейтингу:')
top3_students = sorted(marks.items(), key=lambda x: sum(x[1]), reverse=True)[:3]
[print(f'{i[0]} : {sum(i[1])}') for i in top3_students]

print('Топ 3 самых сложных заданий:')
tasks_hardnes = list()
for i in range(tasks_count):
    tasks_hardnes.append(0)
    for student in student_names:
        tasks_hardnes[i] += marks[student][i]
top3_tasks = sorted(enumerate(tasks_hardnes), key=lambda x : x[1])[:3]
[print(f'{i[0]+1} : {i[1]}') for i in top3_tasks]

