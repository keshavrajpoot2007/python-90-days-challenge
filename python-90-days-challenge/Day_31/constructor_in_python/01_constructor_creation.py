class Constructor:
    
    def __init__(self):
        self.message = "I am a constructor"
    
cons = Constructor()
print(cons.message)
    
# The __init__() method acts as a constructor. It needs a mandatory argument named self, which is the reference to the object.