class Addition:
    def add(a, b):
        return a + b

class Substraction:
    def subtract(a, b):
        return a - b

class Multiplication:
    def multiply(a, b):
        return a * b

class Division:
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Math Error")     
    