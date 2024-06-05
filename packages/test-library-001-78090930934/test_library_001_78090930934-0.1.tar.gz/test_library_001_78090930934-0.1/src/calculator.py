from .operations import Addition, Substraction, Multiplication, Division

class Calculator:
    def sum(self, a, b):
        return Addition().add(a, b)
    
    def subs(self, a, b):
        return Substraction().subtract(a, b)
    
    def mult(self, a, b):
        return Multiplication().multiply(a, b)
    
    def div(self, a, b):
        return Division().divide(a, b)