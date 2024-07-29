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
    mycursor.close()
    mydatabase.close()
    
# execute_sql_commands('practice challenges\mydatabase.sql')
class Book:
    def __init__(self, title, author, isbn, quantity):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._quantity = quantity
        self._BookID = None
    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author
    @property
    def isbn (self):
        return self._isbn
    @property
    def quantity(self):
        return self._quantity
    @property
    def BookID(self):
        return self._BookID
    #function that adds books into the database
    def add_books_into_database(self):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Books WHERE isbn = %s AND BookTitle = %s AND BookAuthor = %s AND Quantity = %s'
        check_values = (self.isbn, self.title, self.author, self.quantity)
        mycursor.execute('USE library_db')
        mycursor.execute(check_query, check_values)
        results = mycursor.fetchall()
        if results:
            print ('Book already exists')
        else:
            query = 'INSERT INTO Books(isbn, BookTitle, BookAuthor, Quantity) VALUES(%s,%s,%s, %s)'
            values = (self.isbn, self.title, self.author, self.quantity)
            mycursor.execute(query, values)
            mydatabase.commit()
            self._BookID = mycursor.lastrowid
            print('successfully added book.')
        mycursor.close()
        mydatabase.close()
    @classmethod
    def check_available_books(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'SELECT * FROM Books'
        mycursor.execute('USE library_db')
        mycursor.execute(query)
        results = mycursor.fetchall()
        for result in results:
            print(f"Book ISBN: {result[1]}, Book Title: {result[2]}, Book Author: {result[3]}, Book Quantity: {result[4]}")
        mycursor.close()
        mydatabase.close()
    @staticmethod
    def delete_book_from_database(*args):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        placeholders = ', '.join(['%s'] * len(args))
        query = f'DELETE FROM Books WHERE BookID IN ({placeholders})'
        mycursor.execute('USE library_db')
        mycursor.execute(query, args)
        mydatabase.commit()
        print('successfully deleted')
        
        
        mycursor.close()
        mydatabase.close()
    def __repr__(self) -> str:
        return f"{self.title} by {self.author}, ISBN: {self.isbn} and Quantity of Books: {self.quantity}"
        
class Member:
    member_count = 0
    def __init__(self, name):
        self._name = name
        self._member_id = None
    @property
    def name(self):
        return self._name
    @property
    def member_id(self):
        return self._member_id
    @classmethod
    def increment_member(cls):
        cls.member_count+=1
    def add_member_into_database(self):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Members WHERE MemberName = %s'
        check_values = (self.name, )
        mycursor.execute('USE library_db')
        mycursor.execute(check_query, check_values)
        results = mycursor.fetchall()
        if results:
            print("Member Name already exists")
        else:
            query = 'INSERT INTO Members(MemberName) VALUES(%s)'
            values = (self.name, )
            
            mycursor.execute(query, values)
            mydatabase.commit()
            self._member_id = mycursor.lastrowid
            print('successfully addded member.')
            Member.increment_member()
        mycursor.close()
        mydatabase.close()
    def borrow_book(self, isbn):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'SELECT Quantity FROM Books WHERE isbn = %s'
        values = (isbn, )
        mycursor.execute('USE library_db')
        mycursor.execute(query, values)
        results = mycursor.fetchone()
        if results and results[0]>0:
            inner_query = 'UPDATE Books SET Quantity = Quantity - 1 WHERE isbn = %s'
            innervalues = (isbn, )
            mycursor.execute(inner_query, innervalues)
            mydatabase.commit()
            borrowed_books = []
            borrow_query = 'SELECT BookTitle, BookAuthor FROM Books where isbn = %s'
            borrowed_value = (isbn, )
            mycursor.execute(borrow_query,borrowed_value)
            results = mycursor.fetchone()
            if results:
                borrowed_book = {
                'Book Title': results[0],
                'Book Author': results[1]}
            borrowed_books.append(borrowed_book)
            print(f'{self.name} borrowed {borrowed_books}')
        else:
            print(f'Book with ISBN {isbn} is not available.')
        mycursor.close()
        mydatabase.close()
    def return_book(self, isbn):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'UPDATE Books SET Quantity = Quantity + 1 WHERE isbn = %s'
        values = (isbn, )
        mycursor.execute('USE library_db')
        mycursor.execute(query, values)
        mydatabase.commit()
        borrowed_books = []
        borrow_query = 'SELECT BookTitle, BookAuthor FROM Books where isbn = %s'
        borrowed_value = (isbn, )
        mycursor.execute(borrow_query,borrowed_value)
        results = mycursor.fetchone()
        if results:
            returned_book = {
            'Book Title': results[0],
            'Book Author': results[1]}
            borrowed_books.remove(returned_book)
        print(f'{self.name} returned {borrowed_books}')
        mycursor.close()
        mydatabase.close()
    @classmethod
    def check_available_members_in_database(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'SELECT * FROM Members'
        mycursor.execute('USE library_db')
        mycursor.execute(query)
        results = mycursor.fetchall()
        for result in results:
            print(f"Member ID: {result[0]} Member Name: {result[1]}")
        mycursor.close()
        mydatabase.close()
    @staticmethod
    def delete_member_from_database(*args):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        placeholders = ', '.join(['%s'] * len(args))
        query = f'DELETE FROM Members WHERE Member_id IN ({placeholders})'
        mycursor.execute('USE library_db')
        mycursor.execute(query, args)
        mydatabase.commit()
        print('successfully deleted')
        
        
        mycursor.close()
        mydatabase.close()
    def update_details_for_members(self, name, new_value):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_name = 'SELECT Member_id from Members WHERE MemberName = %s'
        values = (name, )
        mycursor.execute('USE library_db')
        mycursor.execute(check_name,values)
        results = mycursor.fetchone()
        if results:
            query = 'UPDATE Members SET Member_id = %s WHERE MemberName = %s'
            myvalue = (new_value, name)
            mycursor.execute(query, myvalue)
            mydatabase.commit()
            print('updated successfully')
        else:
            print('no member with such a name')
        mycursor.close()
        mydatabase.close()
    def __repr__(self) -> str:
        return f"Member Name:  {self.name} Member ID: {self.member_id}"


# execution
