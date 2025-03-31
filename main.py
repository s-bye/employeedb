from classes.employee import Employee
from classes.employeeDAO import EmployeeDAO

dao = EmployeeDAO("employee.db")

emp_1 = Employee(id=None, name="Imanbek Mashrapov", position="Data Scientist", salary=100000, hire_date="2026_05_05")
emp_id = dao.insert_table(emp_1)
print(dao.get_by_id(emp_id))