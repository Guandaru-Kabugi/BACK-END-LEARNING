from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name","surname","email")
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","isbn","publication_year")

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name",)
@admin.register(BookRequest)
class BookRequestAdmin(admin.ModelAdmin):
    list_display=("user","book_borrowed","requested_date")
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display=("user","role")