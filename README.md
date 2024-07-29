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