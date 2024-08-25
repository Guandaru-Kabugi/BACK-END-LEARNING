from django.test import TestCase,SimpleTestCase
from .models import Book, Author, UserProfile,Library,BookRequest
from django.urls import reverse
from django.contrib.auth.models import User
from .views import *

# Create your tests here.

class ModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_case',email='kabugi87@gmail.com')
        self.user.set_password = ('Alex123..')
        self.user_profile = UserProfile.objects.create(user=self.user, role='Member')
        self.user.save()
        self.author = Author.objects.create(first_name='Alex',second_name='Kabugi',surname='Guandaru',email='kb898@gmail.com')
        self.book = Book.objects.create(title="Sample Book",
            author=self.author,
            isbn="1234567890",
            publication_year="2023-01-01",)
        self.library = Library.objects.create(name='ALX')
        self.library.books.add(self.book)
        self.request = BookRequest.objects.create(book_borrowed = self.book, user=self.user)
    def test_book_creation(self):
        self.assertEqual(self.book.title, "Sample Book")
        self.assertEqual(self.book.author.first_name,"Alex")
        self.assertEqual(self.book.isbn,"1234567890")
        self.assertEqual(self.user_profile.role, "Member")
        self.assertEqual(self.user.username, "test_case")
        self.assertEqual(self.request.book_borrowed, self.book)
        self.assertEqual(self.request.user, self.user)
    def test_views_creation(self):
        self.client.login(username='test_case',password='Alex123..')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        pass
    

