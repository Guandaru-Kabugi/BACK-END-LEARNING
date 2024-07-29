from library_management_system import *


book1 = Book("The Wall Speaks", "Jerr", "9898918287837", 10)
book2 = Book("1984", "George Orwell", "0451524934", 15)
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", 8)
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 12)
book5 = Book("Moby Dick", "Herman Melville", "9781503280786", 7)
book6 = Book("Pride and Prejudice", "Jane Austen", "9781503290563", 9)
books = [book1, book2, book3, book4, book5, book6]


member1 = Member('Kabugi')
member2 = Member('Grace')
member3 = Member ('Ann')
member4 = Member('Brian')
member5 = Member('Pauline')
member6 = Member('James')
members = [member1, member2, member3, member4, member5, member6]
# member6.add_member_into_database()
# for member in members:
#     member.add_member_into_database()
# Book.check_available_books()
# print(Member.member_count)
# Member.delete_member_from_database(12,13)
# Member.check_available_members_in_database()

# Member.check_available_members_in_database()

def user_control_interface():
    print("Welcome to My Library")
    continue_asking = True
    while continue_asking:
        user_choice = int(input("Select 1 to add Member, Select 2 to See all Books,Select 3 to update member details, Select 4 to See all Members, Select 5 to delete member, select 6 to borrow book, select 7 to return book, select 8 to check number of members, select 9 to exit:" ))
        match user_choice:
            case 1:
                member_name = input("Please input your name: ")
                member = Member(member_name)
                member.add_member_into_database()
            case 2:
                Book.check_available_books()
            case 3:
                member_name = input("Please input your name: ")
                value = int(input('please input new member id: from 7'))
                member = Member(member_name)
                member.update_details_for_members(member_name, value)
            case 4:
                Member.check_available_members_in_database()
            case 5:
                choice = int(input("Please provide your member id for deletion"))
                Member.delete_member_from_database(choice)
            case 6:
                member_name = input("Please input your name: ")
                isbn = input('provide isbn number')
                member = Member(member_name)
                member.borrow_book(isbn)
            case 7:
                member_name = input("Please input your name: ")
                isbn = input('provide isbn number')
                member = Member(member_name)
                member.borrow_book(isbn)
            case 8:
                print(Member.member_count)
            case 9:
                print('Goodbye')
                continue_asking = False
                os.system('cls')
user_control_interface()