class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Зарплата не может быть меньше нуля")
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
   
    def set_salary(self, value):
        if value < 0:
            raise ValueError("Уровень зарплаты не может быть отрицательным")
        self.__salary = value

    def display_info(self):
        print(f"Имя сотрудника: {self.name}, Заработная плата: {self.__salary}")
        
               
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


dev = Developer("Alice", 5000, "Python")
dev.display_info()
dev.set_salary(-120)
