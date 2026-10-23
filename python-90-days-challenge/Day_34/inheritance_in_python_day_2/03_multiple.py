class Mother:
    def __init__(self, mothername):
        self.mothername = mothername
        
    def MotherDetails(self):
        print("Mother name is:", self.mothername)
        
class Father:
    def __init__(self, fathername):
        self.fathername = fathername
        
    def FatherDetails(self):
        print("Father name is:", self.fathername)
        
class Son(Mother, Father):
    def __init__(self, mothername, fathername, sonname):
        Mother.__init__(self, mothername)
        Father.__init__(self, fathername)
        self.sonname = sonname
        
    def SonDetails(self):
        print("Son name is:", self.sonname)
        
s = Son("Mary", "John", "David")

s.FatherDetails()
s.MotherDetails()
s.SonDetails()