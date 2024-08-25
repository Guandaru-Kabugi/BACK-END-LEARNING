from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as CustomUserAdmin

# Register your models here.
from .models import Book, Author,Librarian,Library, User
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', )
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', )
@admin.register(User)
class UserAdmin(CustomUserAdmin):
    pass