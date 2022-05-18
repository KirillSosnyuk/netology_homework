def whole_avg(person_list, course):
    average_rate = 0
    counter = 0
    for person in person_list:
        if course in person.grades.keys():
            average_rate += sum(person.grades[course])
            counter += len(person.grades[course])
        else:
            return f"У {person.name} {person.surname} нет такого курса."
    return 'Общая оценка: ' + str(round(average_rate / counter, 1))
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecture(self, lecturer, course, *grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            return 'Ошибка'

        
    def average_count(self):
        avg_rating = []
        for average in self.grades.values():
            if len(average) > 0:
                avg_rating.append(sum(average) / len(average))
        if avg_rating != []: # Проверка на присутствие хотя бы одной оценки
            self.average = round((sum(avg_rating) / len(avg_rating)), 1)
            return self.average
        else:
            self.average = 0
            return self.average

    
    def __str__(self):
        # Везде пришлось сделать return последнюю строчку, так как __str__ требует что-то вернуть.
        # Можно было бы запихнуть в return всё(имя, фамилию и т.д.), однако это отразилось бы на читаемости кода.
        in_progress = ""
        finished = ""
        for courses in range(len(self.courses_in_progress)): # Оформил через циклы, чтобы проставить запятые. В примере они присутствуют.
            in_progress += self.courses_in_progress[courses] + ", "
        in_progress = in_progress[:-2]
        for courses in range(len(self.finished_courses)):
            finished += self.finished_courses[courses] + ", "
        finished = finished[:-2]
        
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        print(f"Средняя оценка за домашние задания: {self.average_count()}")
        print("Курсы в процессе изучения: ", in_progress)
        return "Завершенные курсы: " + finished


    def __lt__(self, other):
        if not isinstance(other, Student) or not isinstance(self, Student):
            print("Ошибка. Сравнение происходит не с лекторами.")
        else:
            return self.average_count() < other.average_count()


                 
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []   
    


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} # Здесь добавил словарь для оценки лекторов
        
    def average_count(self):
        avg_rating = []
        for average in self.grades.values():
            if len(average) > 0:
                avg_rating.append(sum(average) / len(average))
        if avg_rating != []:
            self.average = round((sum(avg_rating) / len(avg_rating)), 1)
            return self.average
        else:
            self.average = 0
            return self.average


    def __str__(self):
        # Везде пришлось сделать return последнюю строчку, так как __str__ требует что-то вернуть.
        # Можно было бы запихнуть в return всё(имя, фамилию и т.д.), однако это отразилось бы на читаемости кода.
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")
        return "Средняя оценка за лекции: " + str(self.average_count())

    
    def __lt__(self, other):
        if not isinstance(other, Lecturer) or not isinstance(self, Lecturer):
            print("Ошибка. Сравнение происходит не с лекторами.")
        else:
            return self.average_count() < other.average_count()



       
class Reviewer(Mentor):
    def rate_hw(self, student, course, *grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

        
    def __str__(self):
        # Везде пришлось сделать return последнюю строчку, так как __str__ требует что-то вернуть.
        # Можно было бы запихнуть в return всё(имя, фамилию и т.д.), однако это отразилось бы на читаемости кода.
        print(f"Имя: {self.name}")
        return f"Фамилия: {self.surname}"



# Создаем студентов
best_student = Student('Ruoy', 'Eman', 'your_gender')
worst_student = Student('Kirill', 'Sosnyuk', 'male')

# Добавляем студентам курсы
best_student.courses_in_progress += ['Python', 'C++']
best_student.finished_courses += ['Basic', "Java", "Delphi"]

worst_student.courses_in_progress += ['C++', 'Java']
worst_student.finished_courses += ['Git']
 
# Добавляем ревьюеров
reviewer_1 = Reviewer("Alex", "Smirnov")
reviewer_2 = Reviewer("Nicolay", "Sidorov")

# Добавляем ревьюерам курсы
reviewer_1.courses_attached += ["Python"]
reviewer_1.courses_attached += ["C++"]

reviewer_2.courses_attached += ["Java"]
reviewer_2.courses_attached += ["C++"]

# Добавляем лекторов
lecturer_1 = Lecturer("Ivan", "Rudkov")
lecturer_2 = Lecturer("Sergei", "Lubov")

# Добавляем лекторам курсы
lecturer_1.courses_attached += ["Python", 'Java']
lecturer_2.courses_attached += ["C++", 'Python']

# Ревьюеры оценивают лекторов
reviewer_1.rate_hw(best_student, 'Python', 10, 10, 10)
reviewer_2.rate_hw(best_student, 'C++', 9, 6, 7)

reviewer_1.rate_hw(worst_student, 'C++', 3, 4, 2)
reviewer_2.rate_hw(worst_student, 'C++', 7, 5, 4)

# Студенты оценивают лекторов
best_student.rate_lecture(lecturer_1, "Python", 10, 6 ,8)
best_student.rate_lecture(lecturer_2, "Python", 7, 4 ,2)
best_student.rate_lecture(lecturer_2, "C++", 7, 7 ,9)

worst_student.rate_lecture(lecturer_2, "Python", 10, 6 ,8)
worst_student.rate_lecture(lecturer_2, "C++", 7, 7 ,9)

#Тестируем вывод студентов, лекторов и ревьюеров
print(best_student, worst_student, sep="\n")
print()
print(reviewer_1, reviewer_2, sep="\n")
print()
print(lecturer_1, lecturer_2, sep="\n")
# Тестируем сравнение лекторов и студентов
print(lecturer_1 > lecturer_2) 
print(best_student < worst_student)

# Cоздаем списки студентов и лекторов для тестирования общего подсчета среднего значения оценки по курсу
students = [best_student, worst_student]
lecturers = [lecturer_1, lecturer_2]

print(whole_avg(students, 'C++')) # Тестируем для студентов
print(whole_avg(lecturers, 'Python'))# Тестируем для лекторов
