import mysql.connector
import os
from dotenv import load_dotenv
from decimal import Decimal
from datetime import date

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')

mydatabase = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASSWORD,
    database = DB_DATABASE
)
mycursor = mydatabase.cursor()
# mycursor.execute('SELECT * FROM Customers')
def create_new_customer(CustomerID, FirstName,LastName,RegistrationDate, Email,Telephone):
    try:
        check_query = 'SELECT * FROM Customers WHERE CustomerID = %s AND FirstName = %s AND LastName = %s AND RegistrationDate = %s AND Email = %s AND Telephone = %s'  
        values = (CustomerID,FirstName,LastName,RegistrationDate,Email,Telephone)
        mycursor.execute(check_query,values)
        result = mycursor.fetchone()
        if result:
            print('Customer details already exists')
        else:
            query = 'INSERT INTO Customers(CustomerID, FirstName,LastName, Email,Telephone) VALUES(%s,%s,%s,%s,%s)'
            values = (CustomerID,FirstName,LastName,Email,Telephone)
            mycursor.execute(query,values)
            mydatabase.commit()
            print("Successfully added new customer")
    except Exception as e:
        print('An error occurred', e)
    finally:
        mycursor.close()
        mydatabase.close()
# create_new_customer(12,'Anen','Kiraa','2023-11-14', mnnyelkira@gmail.com','122-455-1980')
def read_data (table):
    query = f'SELECT * FROM {table}' #for tables we use a string instead of %s
    mycursor.execute(query)
    results = mycursor.fetchall()
    print("Success")
    # for row in results:
    #     print(row)
    for row in results:
            # Convert each element in the row to a string if it's a Decimal or date
            formatted_row = [
                str(element) if isinstance(element, (Decimal, date)) else element 
                for element in row
            ]
            print(tuple(formatted_row))
# read_data('Customers')
def update_data(table, Column, new, CustomerID):
    query = f'UPDATE {table} SET {Column} = %s WHERE CustomerID = %s'
    mycursor.execute(query, (new,CustomerID))
    mydatabase.commit()
    print(mycursor.rowcount,'success')
update_data('Customers', 'LastName', 'Kabs', '11')

def delete_data (table,id):
    query = F'DELETE FROM {table} WHERE CustomerID = %s'
    values = (id, )
    mycursor.execute(query,values)
    mydatabase.commit()
    print('Delete Successful.')
# delete_data('Customers','12')

mycursor.close()
mydatabase.close()
    
print("Database connection closed.")