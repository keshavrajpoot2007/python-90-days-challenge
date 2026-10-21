# Parent Class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")

# Child Class
class HR(Employee):
    def work(self):
        print(f"{self.name} handles recruitment and onboarding.")

hr1 = HR("Raghavi", 101)
hr1.show_details()      
hr1.work() 