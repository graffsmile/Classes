class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        """Определяется средняя оценка за домашние задания и выводится информация:
        print(some_student)
        Имя: Ruoy
        Фамилия: Eman
        Средняя оценка за домашние задания: 9.9
        Курсы в процессе изучения: Python, Git
        Завершенные курсы: Введение в программирование
        """
        grades_count = 0
        courses_in_progress_all = ', '.join(self.courses_in_progress)
        finished_courses_all = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 1)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_rating}\n' \
              f'Курсы в процессе изучения: {courses_in_progress_all}\n' \
              f'Завершенные курсы: {finished_courses_all}'
        return res

    def rate_hw(self, lecturer, course, grade):
        """Реализует возможность выставления оценки лектору, если этот лектор ведет лекции по данному курсу у этого студента
        Принимает на вход переменные rate_hw(self, lecturer, course, grade)"""

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        """Реализует сравнение через операторы "<", ">" студентов между собой по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        """Выводит информацию вида:
            print(some_reviewer)
            Имя: Some
            Фамилия: Buddy
        """
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 1)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        """Реализует сравнение через операторы "<", ">"лекторов между собой по средней оценке за лекции"""
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Реализует возможность выставления оценки студенту за домашние задания,
        если этот проверяющий закреплен за этим студентом по данному курсу,
        или возвращает ошибку.
        Принимает на вход переменные rate_hw(self, student, course, grade)"""

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Выводит информацию вида:
        print(some_lecturer)
        Имя: Some
        Фамилия: Buddy
        Средняя оценка за лекции: 9.9
        """

        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

# Создаем лекторов и закрепляем их за курсом
best_lecturer_1 = Lecturer('John', 'Conor')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Ivan', 'Petrov')
best_lecturer_2.courses_attached += ['Git']

# Создаем проверяющих и закрепляем их за курсом
cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
#cool_reviewer_1.courses_attached += ['Git']

cool_reviewer_2 = Reviewer('Petr', 'Ivanov')
#cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Git']

# Создаем студентов и определяем для них изучаемые и завершенные курсы
student_1 = Student('Ruoy', 'Eman')
student_1.courses_in_progress += ['Python']
#student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Some', 'Buddy')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

# Выставляем оценки лекторам за лекции
student_1.rate_hw(best_lecturer_1, 'Python', 9)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_2.rate_hw(best_lecturer_2, 'Git', 10)
student_2.rate_hw(best_lecturer_2, 'Git', 8)

# Выставляем оценки студентам за домашние задания
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_2.rate_hw(student_1, 'Python', 10)

cool_reviewer_1.rate_hw(student_1, 'Git', 8)
cool_reviewer_2.rate_hw(student_1, 'Git', 10)


cool_reviewer_1.rate_hw(student_2, 'Git', 9)
cool_reviewer_2.rate_hw(student_2, 'Git', 8)

# Выводим характеристики созданных и оцененых студентов в требуемом виде
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}')
print()
print()

# Выводим характеристики созданных и оцененых лекторов в требуемом виде
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}')
print()
print()

# Выводим результат сравнения студентов по средним оценкам за домашние задания
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# Выводим результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} > {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Создаем список студентов
student_list = [student_1, student_2]

# Создаем список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2]


# Создаем функцию для подсчета средней оценки за домашние задания
# по всем студентам в рамках конкретного курса
# в качестве аргументов принимает список студентов и название курса

def student_rating(student_list, course_name):
    """Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    в качестве аргументов принимает список студентов и название курса"""

    sum_all = 0
    count_all = 0
    for stud in student_list:
       if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Создаем функцию для подсчета средней оценки за лекции всех лекторов в рамках курса
# в качестве аргумента принимает список лекторов и название курса

def lecturer_rating(lecturer_list, course_name):
    """Функция для подсчета средней оценки за лекции всех лекторов в рамках курса 
    в качестве аргумента принимает список лекторов и название курса"""

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Выводим результат подсчета средней оценки по всем студентам для данного курса
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех студентов по курсу {'Git'}: {student_rating(student_list, 'Git')}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Git'}: {lecturer_rating(lecturer_list, 'Git')}")
print()