# 1)Write a program to create a class by name Students, and initialize attributes like name, age, 
# and grade while creating an object.
class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

name = input("Enter the name: ")
while True:
    try:
        age = int(input("Enter your age: "))
        break  
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

grade = input("Enter your grade: ")
student1 = Students(name, age, grade)
print(f"name={student1.name},age= {student1.age}, grade={student1.grade}")
