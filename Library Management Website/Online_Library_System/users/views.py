from typing import Any
from django.urls import reverse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Book, Library, UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required,login_required
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
from .forms import AuthorForm, UserCreationForm,BookForm, LibraryForm, BookRequestForm,LibraryAddBookForm
def user_creation(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            return HttpResponseForbidden("Invalid form details")
    else:
        form = UserCreationForm()
    return render(request,"users/user_creation.html", {"form":form})
# @login_required
# @permission_required("users.can_add_author")
def author_add(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            print("Successfully added author")
            return redirect('/library/books/1/')
        else:
            return HttpResponseForbidden('Invalid form input')
    else:
        form = AuthorForm()
    return render(request, 'users/author_add.html', {"form":form})
# @login_required
# @permission_required("users.can_add_book")
def book_add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            print('Successfully added book')
            return redirect('/books/')
        else:
            return HttpResponseForbidden("Invalid Form")
    else:
        form = BookForm()
    return render(request, "users/add_book.html", {"form": form})
# @login_required
def book_request(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == "POST":
        form = BookRequestForm(request.POST, instance=book)
        if form.is_valid():
            book_request = form.save(commit=False)
            book_request.user = request.user
            book_request.book = book
            book_request.save()
            return redirect('/books/books_borrowed/')
        else:
            return HttpResponseForbidden('Invalid form')
    else:
        form = BookRequestForm(instance=book)
    return render(request, 'users/book_request.html', {"form":form, "book":book})
# @login_required
# @permission_required("users.can_edit_book")
def edit_book(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            print('successfully edited book')
            return redirect('/books/')
        else:
            HttpResponseForbidden('invalid form input')
    else:
        form = BookForm(instance=book)
    return render(request, "users/edit_book.html", {"form":form, "book":book})
# @login_required
# @permission_required("users.can_delete_book")
def delete_book(request, id):
    book = Book.objects.get(pk=id)
    if request.method == "POST":
        book.delete()
        print("book deleted successfully")
        return redirect('/books/')
    return render(request, 'users/delete_books.html', {'book':book})
# @login_required
# @permission_required("users.can_delete_user", raise_exception=True)
def delete_member(request, id):
    member = get_object_or_404(UserProfile,user_id=id, role="Member")
    if request.user.userprofile.role == "Librarian":
        member.user.delete()
        print('Member deleted successfully.')
        return redirect('/home/')
    else:
        return HttpResponseForbidden("You do not have access to this page")
# @login_required
# @permission_required('users.can_delete_user', raise_exception=True)
def delete_librarian(request,id):
    librarian = get_object_or_404(UserProfile,user_id=id, role="Librarian")
    if request.user.userprofile.role == "Admin":
        librarian.user.delete()
        print("Librarian deleted succesfully")
        return redirect('/home/')
    else:
        return HttpResponseForbidden("You do not have access to this page.")
class DisplayBooks(DetailView):
    model = Library
    template_name = 'users/books.html'
    context_object_name = 'library'
    # pk_url_kwarg = id
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class LoginView(LoginView):
    template_name = "users/login.html"
class LogOut(LogoutView):
    template_name = "users/logout.html"
def home(request):
    return render(request,'users/home.html')
# def library_add_books(request, id):
#     library = get_object_or_404(Library, pk=id)
#     if request.method == "POST":
#         form = LibraryAddBookForm(request.POST, instance=library)
#         if form.is_valid():
#             form.save()
#             print('Library created successfully')
#             return redirect('')
#         else:
#             return HttpResponseForbidden("Invalid form input")
#     else:
#         form = LibraryAddBookForm(instance=library)
#     return render(request, 'users/library_add.html', {"form":form, "library":library})
# # @login_required
# def library_add(request):
#     if request.method == "POST":
#         form = LibraryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Successfully added library")
#             return redirect('')
#         else:
#             return HttpResponseForbidden('Invalid form')
#     else:
#         form = LibraryForm()
#     return render(request, 'users/library.html', {"form":form})