from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import list_books, ListLibrary,index,SignUpView, LogView,edit_book,delete_book,add_book
from django.contrib.auth.views import LogoutView, LoginView
app_name = 'relationship_app'
urlpatterns = [
    path('log/',LogView.as_view(), name='logon'),
    # path('loggingin/',log, name='logon'),
    path('',index, name='index'),
    path('registration/',SignUpView.as_view(),name='registration'),
    path('books/', list_books, name='books'), 
    path('<int:id>/', ListLibrary.as_view(), name='library'),
    path('logoff/',LogoutView.as_view(next_page='/'), name='logout' ),
    
    # path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout' ),
    # path('logout/',LoginView.as_view(template_name='relationship_app/login.html'), name='login' ),
    path('add_book/',add_book, name='add_book'),
    path('edit_book/<int:id_book>/', edit_book, name='edit_book'),
    path('delete_book/<int:id_book>/', delete_book, name='delete_book'),
]
