# 8) show class method, static method and instance method with simple example. 
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def add(x, y):
        return x + y
        
    @staticmethod
    def subtract(x, y):
        return x - y

    def multiply(self):
        return self.num1 * self.num2

    @classmethod
    def divide(cls, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"


print("Static Method - Add:", Calculator.add(5, 3))  
print("Static Method - Subtract:", Calculator.subtract(10, 4))  
print()

calc = Calculator(6, 2)

print("Instance Method - Multiply:", calc.multiply())  
print()

print("Class Method - Divide:", Calculator.divide(8, 2))  
print("Class Method - Divide by zero:", Calculator.divide(8, 0))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
