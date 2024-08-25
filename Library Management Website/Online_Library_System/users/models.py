from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return f'First_Name: {self.first_name}, Last_Name = {self.surname}'
    class Meta:
        permissions = [('can_add_author', 'Can_add_author')]
    class Meta:
        unique_together = ('first_name', 'second_name','surname','email')
class Book(models.Model):
    title = models.CharField(max_length=150, null=False)
    author = models.ManyToManyField(Author,related_name='books')
    isbn = models.CharField(max_length=100, null=False)
    publication_year = models.DateField()
    # cover_image = models.ImageField(upload_to='covers/', null=True)
    def __str__(self):
        return f"Title: {self.title} by {', '.join(author.first_name for author in self.author.all())}"
    class Meta:
        permissions = [('can_add_book', 'Can_add_book'), ('can_delete_book','Can_delete_book'), ('can_edit_book','Can_edit_book')]
    class Meta:
        unique_together = ('title', 'isbn','publication_year')
class Library(models.Model):
    name = models.CharField(max_length=100, null=False)
    books = models.ManyToManyField(Book, related_name='library')
    def __str__(self):
        return self.name
class BookRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book_borrowed = models.ForeignKey(Book,on_delete=models.CASCADE)
    requested_date = models.DateField(auto_now_add=True)
    class Meta:
        permissions = [('can_borrow_book', 'Can_borrow_book')]
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Member')
    def __str__(self):
        return f'Name: {self.user.username} Role: {self.role}'
    class Meta:
        permissions = [('can_delete_user', 'Can_add_user')]

