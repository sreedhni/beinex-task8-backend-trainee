# Write a program to create a child class Teacher that will inherit the properties from the parent class Staff. 
#     attributes need for staff : role,department, salary 
#     attributes need for teacher: name,age 
#     method in  staff : def print_details() 
# output expected - 
# Name:  Raj 
# Age:  28 
# Role: Teacher 
# Department: Science
class Staff:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def print_details(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)


class Teacher(Staff):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age
name=input("enter the name : ")
age=int(input("enter the age : "))
role=input("enter the role: ")
department=input("enter the department : ")
salary=int(input("enter the salary : "))
teacher = Teacher(name,age,role,department,salary)

print("Name:", teacher.name)
print("Age:", teacher.age)
teacher.print_details()
