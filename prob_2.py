# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

# Solution :

class Calculator:
    # class methods
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b


calc = Calculator()

result_add = calc.add(2, 2)
print(result_add)

result_sub = calc.sub(5, 3)
print(result_sub)

result_mul = calc.mul(4, 3)
print(result_mul)

result_div = calc.div(10, 2)
print(result_div)