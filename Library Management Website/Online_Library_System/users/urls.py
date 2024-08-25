from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = 'users'
urlpatterns = [
    
    path('', home, name='home'),
    path('create_user/',user_creation,name='user_creation'),
    # path('library/<int:id>/',library_add_books,name='library'),
    # path('library/',library_add,name='lib'),
    path('library/add_author/',author_add,name='author_add'),
    path('library/add_book/',book_add,name='add_book'),
    # path('library/request_book/<int:id>/',book_request,name='request_book'),
    path('library/edit_book/<int:id>/',edit_book,name='edit_book'),
    path('library/delete_book/<int:id>/',delete_book,name='delete_book'),
    path('library/delete_member/<int:id>/',delete_member,name='delete_member'),
    path('library/delete_librarian/<int:id>/',delete_librarian, name='delete_librarian'),
    path('library/books/<int:pk>/',DisplayBooks.as_view(),name='books'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogOut.as_view(), name='logout'),

    
]#+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
