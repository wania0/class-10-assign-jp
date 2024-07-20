"""
In this exercise, you will create a Python class named Student to represent students. 
The class should have the following attributes and methods:

Attributes:

name: instance variable
age: instance variable
courses: instance variable
available_courses: class variable -> possible values ["English", "Urdu", "Physics", "Math", "Chemistry"]

Methods:

display_info(): An instance method that displays the student's name and age.
enroll(): An instance method that allows a student to enroll in a course by adding it to their list of enrolled courses.
list_courses(): An instance method that displays all the courses that student is enrolled
list_available_courses(): An instance method that display all the avaiable courses


1. Create three instances of the Student class with different names and ages.

2. enroll the students in courses by calling the enroll method.
make sure student should only enroll in the course that are listing in available course
i.e if user input the course "Islamyat" then program should not allow it

3. call list_courses
4. call list_available_courses

"""

class Student:
    # class variable 
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]
    
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age
        self.courses = []
        
    # instance methods    
    def display_info(self):
        print("Student name is:", self.name , ",", "Student's age is:", self.age)
    
    def enroll(self, course):
        if course in Student.available_courses:
            if course not in self.courses:
                self.courses.append(course)
                print(self.name, "is enrolled in:", course)
            else:
                print("Already enrolled in this course", course)
        else:
            print(course, "course is not available.")
            
    def list_courses(self):
        print(self.name, "is enrolled in these courses:", self.courses)
        
    @ classmethod
    def list_available_courses(cls):
        print("The available courses are:", Student.available_courses)
    
    
std_1 = Student("Ava", 20)
std_2 = Student("Charlie", 18)
std_3 = Student("John", 19)

std_1.display_info()
std_1.enroll("Physics")
std_1.enroll("Islamiat")
std_1.list_courses()

std_2.display_info()
std_2.enroll("Chemistry")
std_2.enroll("Urdu")
std_2.enroll("Math")
std_2.list_courses()

std_3.display_info()
std_3.enroll("Urdu")
std_3.enroll("Urdu")
std_3.enroll("English")
std_3.list_courses()




