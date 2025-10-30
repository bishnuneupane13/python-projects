class Company:
    def __init__(self,c_name):
        self.c_name = c_name

class Employee(Company):
    def __init__(self,c_name,name,role):
        super().__init__(c_name)
        self.name = name
        self.role = role

    def start(self):
            print(f"{self.name} has started working as a {self.role} at {self.c_name}.")

b = Employee("TechCorp", "Alice", "Developer")

b.start()