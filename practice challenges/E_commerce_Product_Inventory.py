import os
from dotenv import load_dotenv
import mysql.connector

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
# def add_column():
#     mydatabase = open_database_connection()
#     mycursor = mydatabase.cursor()
#     query = 'ALTER TABLE Products ADD COLUMN Total INT'
#     mycursor.execute('USE E_Commerce')
#     mycursor.execute(query)
#     mydatabase.commit()
#     print("Successfully created column")
#     mycursor.close()
#     mydatabase.close()
# add_column()
# execute_sql_commands('practice challenges\E_comm.sql')
class Product:
    def __init__(self,name, price, quantity,unit):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._product_id = None
        self._unit = unit
    @property
    def unit(self):
        return self._unit
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def quantity(self):
        return self._quantity
    @property
    def product_id(self):
        return self._product_id
    @price.setter
    def price(self,new_value):
        if new_value<0:
            print('Value cannot be zero.')
        else:
            self.price = new_value
    @quantity.setter
    def quantity(self,newvalue):
        if newvalue < 0:
            print('Value cannot be zero')
        else:
            self.quantity = newvalue
    def add_product_to_database(self):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Products WHERE Name = %s AND Price = %s AND Quantity = %s'
        check_values = (self.name, self.price, self.quantity)
        mycursor.execute('USE E_Commerce')
        mycursor.execute(check_query,check_values)
        results = mycursor.fetchone()
        if results:
            print('Record already exists')
        else:
            
            query = 'INSERT INTO Products (Name,Price,Quantity,Unit) VALUES(%s,%s,%s,%s)'
            values = (self.name,self.price,self.quantity,self.unit)
            mycursor.execute(query,values)
            mydatabase.commit()
            print("Successfully added new product")
            mycursor.close()
            mydatabase.close()
    @classmethod
    def remove_product(cls, id):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'DELETE FROM Products WHERE ProductID = %s'
        value = (id, )
        mycursor.execute('USE E_Commerce')
        mycursor.execute(query,value)
        mydatabase.commit()
        print('Successfully deleted product')
        mycursor.close()
        mydatabase.close()
    @classmethod
    def read_display_inventory(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        query = 'SELECT * FROM Products'
        mycursor.execute('USE E_Commerce')
        mycursor.execute(query)
        results = mycursor.fetchall()
        for result in results:
            print({
                'Product Name':result[1],
                'Product ID':result[0],
                'Product Price':f"KES{result[2]}",
                'Product Quantity':result[3],
                'Product Units':result[4],
                'Product Total':f'{result[5]: .2f}'
            })
        mycursor.close()
        mydatabase.close()
    def total(self):
        pass
    @classmethod
    def update_product_details(cls,choice):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        # choice = int(input("What do you want to update: Select 1 for price and 2 for Quantity:  "))
        if choice == 1:
            new_price = float(input("What is the new price? "))
            product_name = input("Please provide the name of the product: ")
            product_id = int(input("Please provide the id of the product: "))
            price_query = f'UPDATE Products SET Price = {new_price} WHERE ProductID = %s AND Name = %s'
            values = (product_id,product_name)
            mycursor.execute('USE E_Commerce')
            mycursor.execute(price_query,values)
            mydatabase.commit()
            print(f"Successfully added {new_price} to {product_name} product.")
            mycursor.close()
            mydatabase.close()
        elif choice == 2:
            new_quantity = int(input("Please input the updated quantity: "))
            product_name = input("Please provide the name of the product: ")
            product_id = int(input("Please provide the id of the product: "))
            product_query = f'UPDATE Products SET Quantity = {new_quantity} WHERE ProductID = %s AND Name = %s'
            quantity_values = (product_id,product_name)
            mycursor.execute('USE E_Commerce')
            mycursor.execute(product_query,quantity_values)
            mydatabase.commit()
            print(f"Successfully added {new_quantity} to {product_name} product.")
            mycursor.close()
            mydatabase.close()
    def __repr__(self) -> str:
        return f"Product Name: {self.name} ProductID: {self.product_id} Product Price: {self.price} Product Quantity: {self.quantity}"
