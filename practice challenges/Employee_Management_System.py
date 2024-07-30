import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def open_database_connection():
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD
        )
def execute_sql_commands(filename):
    mydatabase = open_database_connection()
    mycursor = mydatabase.cursor()
    with open(filename, 'r') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            if command.strip():
                mycursor.execute(command)
    mydatabase.commit()
    print('success')
    mycursor.close()
    mydatabase.close()
# execute_sql_commands('practice challenges\employeedb.sql')
# my classes
class Employee:
    def __init__(self,name,department_name, salary):
        self._name = name
        self._employee_id = None
        self._department_id = self.fetch_department_id(department_name)
        self._salary = salary
    @property
    def name(self):
        return self._name
    @property
    def employee_id(self):
        return self._employee_id
    @property
    def department_id(self):
        return self._department_id
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, value):
        if value <0:
            raise ValueError("Value cannot be below 0")
        else:
            self._salary = value
    def fetch_department_id(self, departmentname):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT DepartmentID FROM Department_Table WHERE name = %s'
        values = (departmentname, )
        mycursor.execute('USE Employees')
        mycursor.execute(check_query,values)
        
        result = mycursor.fetchone()
        if result:
            return result[0]
        else:
            print('Department ID Not Found')
            mycursor.close()
            mydatabase.close()
    # A method that can retrieve data from the Employee Table
    @classmethod
    def read_data_from_employee_table(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'SELECT * FROM Employee_Table'
        mycursor.execute('USE Employees')
        mycursor.execute(query)
        results = mycursor.fetchall()
        for result in results:
            print(
                {
                    'Employee ID':result[0],
                    'Department ID':result[1],
                    'Employee Name':result[2],
                    'Salary':str(result [3])
                }
            )
        mycursor.close()
        mydatabase.close()
    # a method to update salary
    @staticmethod
    def update_salary(new_salary, id, name):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'UPDATE Employee_Table SET Salary = %s WHERE EmployeeID = %s AND EmployeeName = %s'
        values = (new_salary,id,name)
        mycursor.execute('USE Employees')
        mycursor.execute(query,values)
        mydatabase.commit()
        print("Successfully Updated Salary")
        mycursor.close()
        mydatabase.close()
    @staticmethod
    def delete_remove_employee(ID,NAME):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'DELETE FROM Employee_Table WHERE EmployeeName = %s AND EmployeeID = %s'
        values = (NAME,ID)
        mycursor.execute('USE Employees')
        mycursor.execute(check_query,values)
        mydatabase.commit()
        print('User deleted successfully')
        mycursor.close()
        mydatabase.close()
    def add_employee_into_database(self):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Employee_Table WHERE EmployeeName = %s AND Salary = %s'
        values = (self.name,self.salary)
        mycursor.execute('USE Employees')
        mycursor.execute(check_query,values)
        myresults = mycursor.fetchone()
        if myresults:
            print('Details Already Exists')
        else:
            query = 'INSERT INTO Employee_Table(DepartmentID, EmployeeName, Salary) VALUES(%s,%s,%s)'
            query_values = (self.department_id,self.name,self.salary)
            mycursor.execute(query,query_values)
            mydatabase.commit()
            print('Successfully Added New Employee')
            mycursor.close()
            mydatabase.close()
    def __repr__(self) -> str:
        return f"Employee Name: {self.name} Employee Department_ID: {self.department_id} Employee Salary: {self.salary}"
        
class Department:
    def __init__(self,department_name):
        self._department_name = department_name
        self._department_id = None
    @property
    def department_name(self):
        return self._department_name
    @property
    def department_id(self):
        return self._department_id
    @classmethod
    def read_data_from_department_table(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'SELECT * FROM Department_Table'
        mycursor.execute('USE Employees')
        mycursor.execute(query)
        results = mycursor.fetchall()
        for result in results:
            print(
                {
                    'Department ID':result[0],
                    'Department Name':result[1]
                }
            )
        mycursor.close()
        mydatabase.close()
    def add_department_into_database(self):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Department_Table WHERE Name = %s'
        values = (self.department_name, )
        mycursor.execute('USE Employees')
        mycursor.execute(check_query,values)
        myresults = mycursor.fetchone()
        if myresults:
            print('Details Already Exists')
        else:
            query = 'INSERT INTO Department_Table(Name) VALUES(%s)'
            query_values = (self.department_name, )
            mycursor.execute('USE Employees')
            mycursor.execute(query,query_values)
            mydatabase.commit()
            print('Successfully Added New Department')
            mycursor.close()
            mydatabase.close()
    def __repr__(self) -> str:
        return f"Department Name: {self.department_name} Department_ID: {self.department_id}"