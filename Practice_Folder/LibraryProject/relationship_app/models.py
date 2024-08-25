from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password,date_of_birth):
        if not email:
            raise ValueError("You must have an email")
        if not date_of_birth:
            raise ValueError("You must provide a birth date")
        # if not profile_photo:
        #     raise ValueError("You must provide a profile pic")
        user = self.model(email=self.normalize_email(email),date_of_birth=date_of_birth)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,password,date_of_birth):
        user = self.create_user(email,password,date_of_birth)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    email = models.EmailField(max_length=155, unique=True)
    username = models.CharField(max_length=100, unique=False, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, default=timezone.now)
    # profile_photo = models.ImageField(blank=True)
    
    USERNAME_FIELD = 'email'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
    objects = UserManager()
class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField(null=True)
    def __str__(self):
        return self.title
    class Meta:
        permissions = [("can_add_book", "Can_add_book"),("can_change_book", "Can_change_book"),("can_delete_book", "Can_delete_book")]
    class Meta:
        permissions = [("can_view", "Can_view"),("can_create","Can_create"),("can_edit","Can_edit"),("can_delete","Can_delete")]
    

class Library(models.Model):
    name = models.CharField(max_length=100, null=False)
    books = models.ManyToManyField(Book, related_name='library')
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100, null=False)
    library = models.OneToOneField(Library,on_delete=models.CASCADE)
    def __str__(self):
        return self.name