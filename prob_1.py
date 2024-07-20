# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

# Solution :
 
from datetime import datetime, date 
 
class Person:
    
    def __init__(self, name, country, dob):
        
        self.name = name
        self.country =  country
        self.dob = dob 
        
    def calculate_age(self):
        
        dob_obj = datetime.fromisoformat(self.dob)
        return datetime.today().year - dob_obj.year


person_1 = Person("Wania", "pakistan", "2004-09-18")

age = person_1.calculate_age()

print(person_1.name, "is", age, "years old!")



