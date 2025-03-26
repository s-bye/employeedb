class Employee:
    def __init__(self, id, name, position, salary, hire_date):
        self.id = id
        self.name = name
        self.position = position
        self._salary = salary
        self.hire_date = hire_date

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def __str__(self):
        return f"Employee ID: {self.id} \n Name: {self.name} \n Position: {self.position} \n Salary: {self.salary} \n Hire Date: {self.hire_date}"