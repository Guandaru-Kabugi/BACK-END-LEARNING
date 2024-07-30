from Employee_Management_System import *


def main():
    continue_asking = True
    while continue_asking:
        user_choice = int(input("Select 1 to add New Employee, Select 2 to add New Department, Select 3 to See Department Table, Select 4 to See Employee Table, Select 5 to Update Salary, Select 6 to Delete Employee, Select 7 to Exit:  "))
        match user_choice:
            case 1:
                employee_name = input("What is your name?  ")
                print("Here are all the departments and IDs: ")
                Department.read_data_from_department_table()
                department_name = input("Select your department of choice: ")
                salary = input("please input your salary: ")
                employee = Employee(employee_name,department_name,salary)
                employee.add_employee_into_database()
            case 2:
                deptname = input("please select the name of your department")
                dept = Department(deptname)
                dept.add_department_into_database()
            case 3:
                Department.read_data_from_department_table()
            case 4:
                Employee.read_data_from_employee_table()
            case 5:
                print("Here are all the employees: ")
                Employee.read_data_from_employee_table()
                employeename = input("Please provide Employee Name")
                employeeid = input("Please provide id of employee")
                salary = input("Please provide new salary")
                if salary<0:
                    print("Salary cannot be negative")
                else:
                    Employee.update_salary(salary,employeeid,employeename)
            case 6:
                print("Here are all the employees: ")
                Employee.read_data_from_employee_table()
                employeename = input("Please provide Employee Name")
                employeeid = input("Please provide id of employee")
                Employee.delete_remove_employee(employeeid,employeename)
            case 7:
                print('Goodbye')
                continue_asking = False
                os.system('cls')
            case _:
                print("Invalid choice, please try again.")    
if __name__ == '__main__':
    main()