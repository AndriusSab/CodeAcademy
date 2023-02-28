# Create a Calculator class with main functionality: add, divide, multiply, subtract , etc.. 
# Initiate class and show up some calculations.


class Calculator:
    def __init__(self, numb1:float, numb2: float):
        self.numb1: float = numb1
        self.numb2: float = numb2
    
    def add(self):
        return self.numb1 + self.numb2
    
    def multiply(self):
            return self.numb1* self.numb2
    
    def divide(self):
         return self.numb1/self.numb2
    def subtract(self):
         return self.numb1 - self.numb2
    
numbers = Calculator(10,5)

print(numbers.add())
    
    
 