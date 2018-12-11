# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

count = {}
for student in students:
    for name in student.values():
    # print(name)
        if name in count:
            count[name] += 1
        else:
            count[name] = 1  

for n in count:
    print(n, count[n])   


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

print('==========')

def tr(students):
    counts = {}
    for student in students:
      for name in student.values():
        if name in counts:
          counts[name] += 1
        else:
          counts[name] = 1    

    result=sorted(counts.items(), key = lambda item : item[1])
    answer=(result.pop())
    return(answer[0])
print(f'самое встречающееся имя среди учеников {tr(students)}')

print('==========')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# print(f'само часто имя в классе 1: {tr(school_students[0])}')
# print(f'само часто имя в классе 2: {tr(school_students[1])}')
i=1
for st in school_students:
    counts = {}    
    for student in st:
      for name in student.values():
        if name in counts:
          counts[name] += 1
        else:
          counts[name] = 1    

    result=sorted(counts.items(), key = lambda item : item[1])
    answer=(result.pop())
    print(f'самое встречающееся имя в классе {i} {answer[0]}')
    i+=1

print('==========')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
males = 0
females = 0

for clas in school:
    number_of_clas = clas['class']
    for students in clas['students']:
        # print(students)
        for f_cl in students.values():
            # print(f_cl)       
            if is_male[f_cl]:
                males += 1
            else:
                females += 1           
    print(f'в классе {number_of_clas} {females} девочки и {males} мальчика')
    males,females = (0,0)

print('==========')
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.

# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

males = 0
females = 0

for clas in school:
    number_of_clas = clas['class']
    for students in clas['students']:
        # print(students)
        for f_cl in students.values():
            # print(f_cl)       
            if is_male[f_cl]:
                males += 1
            else:
                females += 1        
    if males > females:
        print(f'Больше всего мальчиков в классе {number_of_clas}')
    else:
        print(f'Больше всего девочек в классе {number_of_clas}')
    males,females = (0,0)

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a