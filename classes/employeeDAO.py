import sqlite3
from classes.employee import Employee

class EmployeeDAO:
    def __init__(self, db_file="employee.db"):
        self.db_file = db_file
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary REAL NOT NULL,
                    hire_date TEXT NOT NULL
                )
            """)
            conn.commit()

    def insert_table(self, employee):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO employee (name, position, salary, hire_date) VALUES (?, ?, ?, ?)",
                           (employee.name, employee.position, employee.salary, employee.hire_date))
            conn.commit()
            employee.id = cursor.lastrowid
        return employee.id

    def get_by_id(self, id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, position, salary, hire_date FROM employee WHERE id = ?", (id,))
            row = cursor.fetchone()
            if row:
                return Employee(id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4])
        return None

    def get_all_id(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, position, salary, hire_date FROM employee")
            rows = cursor.fetchall()
            return [Employee(id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4]) for row in rows]

    def update(self, employee):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE employee
                SET name = ?, position = ?, salary = ?, hire_date = ?
                WHERE id = ?
            """, (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
            conn.commit()

    def delete(self, id):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employee WHERE id = ?", (id,))
            conn.commit()
