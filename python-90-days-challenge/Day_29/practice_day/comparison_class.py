class Comparison:
        
    def greater_num(self, num1, num2):
        if num1 > num2:
            return num1
        
        else:
            return num2
        
    def less_num(self, num1, num2):
        if num1 < num2:
            return num1
                
        else:
            return num2
        

com = Comparison()

print(com.greater_num(4,9))
print(com.less_num(4,9))