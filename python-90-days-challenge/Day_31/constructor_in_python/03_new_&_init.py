class Demo:

  def __new__(cls, *args, **kwargs):
    print("1. __new__ run hua: Object memory me ban raha hai...")
    # Parent class (object) ka __new__ call karke naya instance generate karte hain
    instance = super().__new__(cls)
    return instance

  def __init__(self, name):
    print("2. __init__ run hua: Object me data set ho raha hai...")
    self.name = name


# Object banate hain:
d = Demo("Rahul")
print(f"3. Final Object ready: {d.name}")