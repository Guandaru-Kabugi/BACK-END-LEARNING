# BACK-END-LEARNING

Challenge 1: Library Management System
Objective: Create a simple library management system where you can manage books and members using classes and MySQL for data storage.

Requirements:

Classes: Create classes for Book and Member.
Book:
Attributes: title, author, isbn, quantity
Methods: display_info()
Use @property for title, author, isbn, and quantity to make them read-only.
Member:
Attributes: name, member_id
Methods: borrow_book(), return_book(), display_info()
Use @property for name and member_id to make them read-only.
Class Method: Add a class method to the Member class to count the total number of members.
Database Interaction:
Use MySQL Connector to create a database and tables for books and members.
Implement methods in your classes to add, update, and retrieve data from the database.


Challenge 2: Employee Management System
Objective: Develop an employee management system with classes for managing employees and departments, incorporating MySQL for data storage.

Requirements:

Classes: Create classes for Employee and Department.
Employee:
Attributes: name, employee_id, department_id, salary
Methods: display_info()
Use @property for name, employee_id, department_id, and salary to make them read-only.
Use a setter for salary to ensure it cannot be set to a negative value.
Department:
Attributes: name, department_id
Methods: display_info()
Use @property for name and department_id to make them read-only.
Static Method: Add a static method to the Employee class to validate if a given employee ID is in the correct format (e.g., starts with "EMP" followed by digits).
Database Interaction:
Use MySQL Connector to create a database and tables for employees and departments.
Implement methods in your classes to add, update, and retrieve data from the database.

Challenge 3: E-commerce Product Inventory
Objective: Create an inventory management system for an e-commerce platform using classes and MySQL for data storage.

Requirements:

Classes: Create classes for Product and Inventory.
Product:
Attributes: name, product_id, price, quantity
Methods: display_info()
Use @property for name, product_id, price, and quantity to make them read-only.
Use setters for price and quantity to ensure they cannot be set to negative values.
Inventory:
Attributes: products (a list of Product instances)
Methods: add_product(), remove_product(), display_inventory()
Class Method: Add a class method to the Product class to count the total number of products.
Database Interaction:
Use MySQL Connector to create a database and tables for products.
Implement methods in your classes to add, update, and retrieve data from the database.
Tips for Implementation:
Setup MySQL Connection: Ensure you have MySQL Connector installed and set up a connection to your database.
Database Schema: Design your database schema and create tables accordingly.
CRUD Operations: Implement Create, Read, Update, and Delete operations for your database tables.
Testing: Test your classes and methods to ensure they work correctly and interact with the database as expected.

Challenge 4: Online Learning Platform
Objective: Create an online learning platform system where you manage courses, instructors, and students using inheritance, composition, and MySQL for data storage.

Requirements:

Classes:
Person (Base class):
Attributes: name, email
Methods: display_info()
Use @property for name and email to make them read-only.
Instructor (Inherits from Person):
Attributes: instructor_id, courses (a list of Course instances)
Methods: add_course(), remove_course(), display_courses()
Use @property for instructor_id to make it read-only.
**Use a setter for email to ensure it follows a valid email format.**
Student (Inherits from Person):
Attributes: student_id, courses (a list of Course instances)
Methods: enroll_course(), drop_course(), display_courses()
Use @property for student_id to make it read-only.
Course:
Attributes: course_id, course_name, instructor (an instance of Instructor)
Methods: display_info()
Use @property for course_id and course_name to make them read-only.
Composition:
The Instructor class should have a list of Course instances, representing the courses they teach.
The Student class should have a list of Course instances, representing the courses they are enrolled in.
**Class Method: Add a class method to the Course class to count the total number of courses available.**
Database Interaction:
Use MySQL Connector to create a database and tables for persons, instructors, students, and courses.
Implement methods in your classes to add, update, and retrieve data from the database.
Tips for Implementation:
Setup MySQL Connection: Ensure you have MySQL Connector installed and set up a connection to your database.
Database Schema: Design your database schema and create tables accordingly.
CRUD Operations: Implement Create, Read, Update, and Delete operations for your database tables.
Testing: Test your classes and methods to ensure they work correctly and interact with the database as expected.
This challenge will help you practice inheritance, composition, and database interactions, reinforcing your understanding of object-oriented programming concepts along with MySQL in Python.