from abc import ABC, abstractmethod

# Abstraction: Using ABC (Abstract Base Class) to define a blueprint
class Employee(ABC):
    
    # Class Variable: Shared across all instances of the class
    company_name = "TechNova Solutions"
    total_employees = 0

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        Employee.total_employees += 1

    # Abstract Method: Must be implemented by any child class
    @abstractmethod
    def calculate_pay(self):
        pass

    def get_details(self):
        return f"[{self.emp_id}] {self.name} at {self.company_name}"


# Inheritance: FullTimeEmployee inherits from Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id)
        
        # Encapsulation: Prefixing with '__' makes these variables private
        self.__base_salary = salary 
        self.__bonus = 0            

    # Encapsulation (Setter): Safely modifying private variables
    def award_bonus(self, amount):
        if amount > 0:
            self.__bonus = amount
        else:
            print("Bonus must be a positive amount.")

    # Encapsulation (Getter): Safely accessing private variables
    def get_salary_details(self):
        return self.__base_salary + self.__bonus

    # Implementing the abstract method from the parent class
    def calculate_pay(self):
        return self.get_salary_details()


# --- Execution ---

# 1. Instantiate objects
emp1 = FullTimeEmployee("Alice Smith", "E001", 85000)
emp2 = FullTimeEmployee("Bob Jones", "E002", 90000)

# 2. Demonstrate Encapsulation
emp1.award_bonus(5000)
# print(emp1.__base_salary)  <-- This would raise an AttributeError because it is hidden

# 3. Demonstrate Inheritance and Abstraction
print(emp1.get_details())
print(f"Total Pay: ${emp1.calculate_pay()}")

# 4. Demonstrate Class Variable
print(f"Total Employees created: {Employee.total_employees}")