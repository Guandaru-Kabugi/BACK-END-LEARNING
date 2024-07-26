import os
from dotenv import load_dotenv
import mysql.connector
import difflib

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
mydatabase = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USER,
    password = DB_PASSWORD,
    database = 'LibraryManagementSystem'
)

mycursor = mydatabase.cursor()

def create_row_of_data_into_table(TITLE, AUTHOR, ISBN):
    check_query = 'SELECT * FROM Books WHERE BookTitle = %s AND BookAuthor = %s AND ISBN = %s'
    value = (TITLE,AUTHOR,ISBN)
    mycursor.execute(check_query,value)
    results = mycursor.fetchone()
    if results:
        print('details already exists')
    else:
        query = 'INSERT INTO Books (BookTitle,BookAuthor,ISBN) VALUES (%s,%s,%s)'
        values = (TITLE,AUTHOR,ISBN)
        mycursor.execute(query,values)
        mydatabase.commit()
        print('Successfully added')
        
# create_row_of_data_into_table("The Book Thief", "Markus Zusak", "9780375842207")

# Searching Books:Write a function that allows users to search for books by title. \
    # It should use a SELECT query with a WHERE clause to filter results based on the user’s input. \
        # Print the details of any matching books.
def search_data_from_table():
    choice = (input("Select 1 to search based on title and 2 to search based on ISBN: "))
    if not choice.isdigit():
        print('Value needs to be integers')
        return
    else:
        choice = int(choice)

        try:
            choice = int(choice)
            # if not isinstance(choice, int):
            #     raise ValueError('Only use Integers')
            if choice not in [1,2]:
                print ('Choice must only be either 1 or 2')
                return
            if choice == 1:
                inputvalue = input("Type the title of the book you want: ").strip()
                query = 'SELECT * FROM Books WHERE BookTitle = %s'
                values = (inputvalue, )
                mycursor.execute(query,values)
                results = mycursor.fetchone()
                if results:
                    print(results)
                else:
                    print('Exact match not found. Finding closest matches...')
                    
                    query = 'SELECT BookTitle FROM Books'
                    mycursor.execute(query)
                    all_titles = mycursor.fetchall()
                    
                    # Extract titles from the query result
                    all_titles = [title[0] for title in all_titles]
                    
                    # Find the closest matches
                    closest_matches = difflib.get_close_matches(inputvalue, all_titles)
                    
                    if closest_matches:
                        print('Did you mean:')
                        for match in closest_matches:
                            # Retrieve full details for each close match
                            query = 'SELECT BookTitle, BookAuthor, ISBN FROM Books WHERE BookTitle = %s'
                            values = (match,)
                            mycursor.execute(query, values)
                            book_details = mycursor.fetchall()
                            for book in book_details:
                                print(book)
                    else:
                        raise ValueError('Sorry Book not available')
            elif choice == 2:
                inputvalue = input ("Type the ISBN of the book you want: ").strip()
                query = 'SELECT * FROM Books WHERE ISBN = %s'
                values = (inputvalue, )
                mycursor.execute(query,values)
                results = mycursor.fetchone()
                if results:
                    print(results)
                else:
                    raise ValueError('Sorry Book not available')
            
                
        except Exception as e:
            print(e)
            print("Here is the list of book titles and ISBN")
            query = 'SELECT BookTitle, ISBN From Books'
            mycursor.execute(query)
            results = mycursor.fetchall()
            for i in results:
                print(i)
# search_data_from_table()
# Listing All Books: Create a function that retrieves all book information from the books table using a SELECT query. Print the details of all books in a user-friendly format.
def read_data_from_table():
    query = 'SELECT * FROM Books'
    mycursor.execute(query)
    myresults = mycursor.fetchall()
    for i in myresults:
        print(f'Book title: {i[1]} by Author: {i[2]} and has an ISBN Number: {i[3]}')
read_data_from_table()
# (Bonus Challenge: Implement functionality to delete a book from the library by its ID. Use a DELETE query with a WHERE clause to remove the specified book.
def delete_data_from_table(id):
    query = 'DELETE FROM Books WHERE BookID = %s'
    values = (id, )
    mycursor.execute(query, values)
    mydatabase.commit()
    print('Deletion a success.')
# delete_data_from_table(9)
mycursor.close()
mydatabase.close()
    