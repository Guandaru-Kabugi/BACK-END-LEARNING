from typing import Any
from django import forms
from .models import Book, BookRequest,UserProfile, Author, Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class LibraryAddBookForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ("books",)

class LibraryForm(forms.ModelForm):
    
    class Meta:
        model = Library
        fields = ("name","books")

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ("title","author","isbn","publication_year") #"cover_image"
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        isbn = cleaned_data.get('isbn')
        publication_year = cleaned_data.get('publication_year')
        if Book.objects.filter(title=title,author=author,isbn=isbn,publication_year=publication_year).exists():
            raise ValidationError("Ensure details are unique.")
        return 

class BookRequestForm(forms.ModelForm):
    
    class Meta:
        model = BookRequest
        fields = ("book_borrowed", "user", ) 
        exclude = ("requested_date", )
    
class UserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "role")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        if commit:
            user.save()
            # Create and link UserProfile
            UserProfile.objects.create(user=user, role=self.cleaned_data['role'])
        return user
class AuthorForm(forms.ModelForm):
    class Meta:
        
        model = Author
        fields = ("first_name","second_name","surname","email")
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        second_name = cleaned_data.get('second_name')
        surname = cleaned_data.get('surname')
        email = cleaned_data.get('email')
        if Author.objects.filter(first_name=first_name,second_name=second_name,surname=surname,email=email).exists():
            raise ValidationError("An author with this name already exists.")
        return cleaned_data