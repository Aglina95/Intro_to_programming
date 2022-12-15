# Write your code here :-)
class Course:
    def __init__(self, name, ects, period):
        self.name = name
        self.ects = ects
        self.period = period

class Teacher:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.courses = []

    def teach_course(self, course):
        self.courses.append(course)

    def print_course_list(self):
        print(f"{self.name} teaches the following courses:")
        for course in self.courses:
            print(f"In {course.period} he teaches {course.name}")

class Student:
    def __init__(self, name, email, student_id, programme):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.programme = programme
        self.courses = [] # collect the courses of a student
        self.grades = {} # collect the grades of a student

    def add_course(self, course):
        self.courses.append(course)  # add the course to the list of courses

    def print_course_list(self):
        print(f"{self.name} has the following courses:")
        for course in self.courses:
            print(f"In {course.period}, {self.name} has {course.name} ({course.ects} ECTS)")

    def add_grade(self, course, grade):
        self.grades[course] = grade  # add the grade (overwrite an existing grade)

    def has_passed_course(self, course):
        if course in self.grades: # course must be present in grades to have passed it
            if self.grades[course] > 0: # the grade must be more than 0
                return True
        return False


ip2022 = Course("Introduction to Programming", 7.5, "Autumn 2022")
af2023 = Course("Algorithmic Fairness", 7.5, "Spring 2023")
st2022 = Course("Society and Technology", 15, "Autumn 2022")
teacher_martin = Teacher("Martin", "maau@itu.dk")
teacher_martin.teach_course(ip2022)
teacher_martin.teach_course(af2023)
teacher_martin.print_course_list()
cornelius = Student("Cornelius Theodorius", "coth@itu.dk", 12345, "GBI")
cornelius.add_course(st2022)
cornelius.add_course(ip2022)
cornelius.print_course_list()
cornelius.add_grade(ip2022, -3)
print(cornelius.has_passed_course(ip2022))
cornelius.add_grade(ip2022, 7)
print(cornelius.has_passed_course(ip2022))
