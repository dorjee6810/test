class Person:
    def _init_(self, name, age, cid_number):
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


class Teacher(Person):
    def _init_(self, name, age, cid_number, subject, salary, department, designation):
        super()._init_(name, age, cid_number)
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


class Student(Person):
    def _init_(self, name, age, cid_number, student_id, course, year, gpa):
        super()._init_(name, age, cid_number)
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
# Creating objects
teacher1 = Teacher("dorji", 35, "CID11107007659", "Mathematics", 50000, "Math Department", "Professor")
student1 = Student("sonam", 20, "CID11106799036", "S1234", "Computer Science", 2, 3.)

# Example usage
teacher1.walk()
teacher1.talk()
teacher1.teach()
student1.study()
student1.write_exam()