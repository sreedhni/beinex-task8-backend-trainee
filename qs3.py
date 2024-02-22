# 3)Write a Python class, Square, and define two methods that return the square area and perimeter. 

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return 4 * self.length


while True:
    try:
        length = float(input("Enter the length in cm: "))
        break  
    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")

obj1 = Square(length)

print("Area of the square in cm**2:", obj1.area())
print("Perimeter of the square in cm:", obj1.perimeter())
