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

def get_valid_score():
    while True:
        try:
            score = int(input("Enter the score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid mark! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid integer score.")

name1 = input("Enter the name: ")
score1 = get_valid_score()
name2 = input("Enter the name: ")
score2 = get_valid_score()

student1 = Student(name1, score1)
student2 = Student(name2, score2)

print("\nStudent 1:")
student1.display()
print("\nStudent 2:")
student2.display()
print("\nStudent 1 Data as Dictionary:")
print(student1.as_dict())
print("\nStudent 2 Data as Dictionary:")
print(student2.as_dict())
