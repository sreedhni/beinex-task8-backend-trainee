class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.score >= 90:
            return "A+"
        elif 80 <= self.score < 90:
            return "A"
        elif 70 <= self.score < 80:
            return "B+"
        elif 60 <= self.score < 70:
            return "B"
        elif 50 <= self.score < 60:
            return "C+"
        elif 40 <= self.score < 50:
            return "C"
        else:
            return "FAILED"

    def display(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Grade:", self.grade)

    def as_dict(self):
        return {
            'name': self.name,
            'score': self.score,
            'grade': self.grade
        }
name1=input("enter the name: ")
score1=int(input("enter the score: "))
name2=input("enter the name: ")
score2=int(input("enter the score: "))

student1 = Student(name1,score1)
student2 = Student(name2,score2)

print("Student 1:")
student1.display()
print("\nStudent 2:")
student2.display()
print("\nStudent 1 Data as Dictionary:")
print(student1.as_dict())
print("\nStudent 2 Data as Dictionary:")
print(student2.as_dict())
