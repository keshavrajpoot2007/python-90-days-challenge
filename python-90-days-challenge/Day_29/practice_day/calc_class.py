class Calc:
    
    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def mult(self, num1, num2):
        return num1 * num2
    
    def power(self, num1, num2):
        return num1 ** num2
    
    
my_calc = Calc()

print(my_calc.add(4,2))
print(my_calc.sub(4,2))
print(my_calc.mult(4,2))
print(my_calc.power(4,2))