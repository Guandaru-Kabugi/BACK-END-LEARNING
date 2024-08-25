import mysql.connector
from dotenv import load_dotenv
import os

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


def insert_into_database(name):
    mydatabase = open_database_connection()
    mycursor = mydatabase.cursor()
    query = 'INSERT INTO trial1(name) VALUES (%s)'
    values = (name, )
    mycursor.execute('USE trial')
    mycursor.execute(query, values)
    mydatabase.commit()
    print('Success')
    mycursor.close()
    mydatabase.close()
    
insert_into_database('yesme')