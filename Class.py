class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child class: Student
class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

# Child class: Teacher
class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")
student = Student(name="Dorjee", age=20, cid_number="CID11511002795", student_id="ID02230062", course="Electrical", year=2, gpa=3.8)
print(f"Student: {student.name}, Age: {student.age}, CID: {student.cid_number}, Student ID: {student.student_id}, Course: {student.course}, Year: {student.year}, GPA: {student.gpa}")
student.walk()
student.talk()
student.eat()
student.sleep()
student.study()
student.attend_class()
student.write_exam()

print("\n")

# Teacher object
teacher = Teacher(name="Mr. Sonam", age=27, cid_number="CID11500298", subject="CSF", salary=50000, department="Electrical", designation="Lecturer")
print(f"Teacher: {teacher.name}, Age: {teacher.age}, CID: {teacher.cid_number}, Subject: {teacher.subject}, Salary: {teacher.salary}, Department: {teacher.department}, Designation: {teacher.designation}")
teacher.walk()
teacher.talk()
teacher.eat()
teacher.sleep()
teacher.teach()
teacher.grade_students()
teacher.attend_meeting()