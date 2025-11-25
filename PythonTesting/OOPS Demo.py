class Calculator:
    num = 100  #class variables
    #default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())


class BasicCalculator:

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def addition(self):
        return self.firstNumber + self.secondNumber

    def subtraction(self):
        return self.firstNumber - self.secondNumber

    def multiplication(self):
        return self.firstNumber * self.secondNumber

    def division(self):
        return self.firstNumber / self.secondNumber


obj = BasicCalculator(10, 5)
print("Addition:", obj.addition())
print("Subtraction:", obj.subtraction())
print("Multiplication:", obj.multiplication())
print("Division:", obj.division())
