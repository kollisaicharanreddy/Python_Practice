class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.base_salary + self.bonus

manager = Manager("Charan", 50000, 10000)
print(manager.calculate_pay())