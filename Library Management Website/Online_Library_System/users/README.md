Project Structure
Models:

User: Extend the default User model to include roles.
Book: Information about books (title, author, ISBN, etc.).
BookRequest: Tracks member requests for books.
LibrarianProfile: Additional information specific to librarians.
AdminProfile: Additional information specific to admins (if needed).
User Roles:

Member: Can view the list of books and request access.
Librarian: Can add new books to the library.
Admin: Can add librarians and manage the system.

from django.urls import path
from . import views

urlpatterns = [
    path('user_creation/', views.user_creation, name='user_creation'),
    path('add_author/', views.author_add, name='author_add'),
    path('add_book/', views.book_add, name='book_add'),
    path('request_book/<int:id>/', views.book_request, name='book_request'),
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('delete_member/<int:id>/', views.delete_member, name='delete_member'),
    path('delete_librarian/<int:id>/', views.delete_librarian, name='delete_librarian'),
    path('books/<int:pk>/', views.DisplayBooks.as_view(), name='display_books'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    # Add more paths as needed
]

1. ensure you add if authentications for the html
2. add options for forgot password.
3. grant permissions on admin page.
4. ensure users cannot add the same book or author
