from typing import Any
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import DetailView,TemplateView,ListView, CreateView
from .models import Librarian,Library,Author,Book
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from .forms import BookForm,CustomUserCreationForm,CustomLoginForm
from django.contrib.auth.models import auth

# Create your views here.
@permission_required('relationship_app.can_view', raise_exception=True)
def view_book(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'relationship_app/functionview.html',context)
@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form':form})
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, id_book):
    book = Book.objects.get(pk=id_book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid:
            form.save()
            return redirect('/books/')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, id_book):
    book = Book.objects.get(pk=id_book)
    if request.method == 'POST':
        book.delete()
        return redirect('/books/')
    return render(request, 'relationship_app/edit_book.html', {'book': book})
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form':form})
@permission_required('relationship_app.can_change_book')
def edit_book(request, id_book):
    book = Book.objects.get(pk=id_book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid:
            form.save()
            return redirect('/books/')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})
@permission_required('relationship_app.can_delete_book')
def delete_book(request, id_book):
    book = Book.objects.get(pk=id_book)
    if request.method == 'POST':
        book.delete()
        return redirect('/books/')
    return render(request, 'relationship_app/edit_book.html', {'book': book})
@login_required
def list_books (request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'relationship_app/functionview.html',context)

class ListLibrary(DetailView):
    model = Library
    template_name = 'relationship_app/classview.html'
    context_object_name = 'library'
    pk_url_kwarg = 'id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
user = get_user_model()
class SignUpView(CreateView):
    model = user
    form_class = CustomUserCreationForm
    template_name = 'relationship_app/registration.html'
    success_url = reverse_lazy('index')

class LogView(LoginView):
    user = get_user_model()
    model = user
    form_class = CustomLoginForm
    template_name = 'relationship_app/logon.html'
    success_url = reverse_lazy('/')
    
def index(request):
    return render(request, 'relationship_app/index.html')
# def log (request):
#     if request.method == 'POST':
#         form = CustomLoginForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             print(f"Authenticating with email: {email}, password: {password}")
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('/')  #redirects user towards the books page.
#             else:
#                 return HttpResponse("Invalid credentials", status=401)
#         else:
#             return HttpResponse("Invalid form data", status=400)
#     else:
#         form = CustomLoginForm()
#     return render(request, 'relationship_app/logon.html', {'form': form})