class GrandParent:
    def __init__(self, grandparent_name):
        self.grandparent_name = grandparent_name

    def display_grandparent(self):
        print(f"Grandparent Name: {self.grandparent_name}")
        
        
class Parent(GrandParent):
    def __init__(self, grandparent_name, parent_name):
        super().__init__(grandparent_name)
        self.parent_name = parent_name
        
    def display_parent(self):
        print(f"Parent Name: {self.parent_name}")
        
class Child(Parent):
    def __init__(self, grandparent_name, parent_name, child_name):
        super().__init__(grandparent_name, parent_name)
        self.child_name = child_name
        
    def display_child(self):
        print(f"Child Name: {self.child_name}")
        
        
gp = GrandParent("John")
gp.display_grandparent()  # Output: Grandparent Name: John

p = Parent("John", "Michael")
p.display_grandparent()  # Output: Grandparent Name: John
p.display_parent()  # Output: Parent Name: Michael      

c = Child("John", "Michael", "Alice")
c.display_grandparent()  # Output: Grandparent Name: John
c.display_parent()  # Output: Parent Name: Michael
c.display_child()  # Output: Child Name: Alice
        
# class Parent(GrandParent):
#     def __init__(self, parent_name):
#         self.parent_name = parent_name
        
#     def display_parent(self):
#         print(f"Parent Name: {self.parent_name}")
        
# class Child(Parent):
#     def __int__(self, child_name):
#         self.child_name = child_name
        
#     def display_child(self):
#         print(f"Child Name: {self.child_name}")
        
# gp = GrandParent("John")
# gp.display_grandparent()  # Output: Grandparent Name: John

# p = Parent("Michael")
# p.display_parent()  # Output: Parent Name: Michael

# c = Child("Alice")
# c.display_child()  # Output: Child Name: Alice

