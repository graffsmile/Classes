class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
       
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


class Reviewer(Mentor):
    def __init__(self, grade):
        self.grade = grade

 
best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python']
 
cool_mentor_1 = Mentor('Some', 'Buddy')
cool_mentor_1.courses_attached += ['Python']

cool_mentor_2 = Mentor('John', 'BonJovi')
cool_mentor_2.courses_attached += ['Python']
 
cool_mentor_1.rate_hw(best_student_1, 'Python', 10)
cool_mentor_2.rate_hw(best_student_1, 'Python', 9)

print(best_student_1.grades)