from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError("You must have an email")
        user = self.model(email=self.normalize_email(email),**extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def _create_user(self, email, password, **extrafields):
        extrafields.setdefault('is_staff', False)
        extrafields.setdefault('is_superuser', False)
        return self.create_user(email,password,**extrafields)
    def create_superuser(self, email, password, **extrafields):
        """user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user"""
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        return self.create_user(email,password,**extrafields)
class User(AbstractUser,PermissionsMixin):
    email = models.EmailField(max_length=155, unique=True)
    username = models.CharField(max_length=100, unique=False)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username or self.email.split('@')[0]
'''
class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name=None, last_name=None):
        if not email:
            raise ValueError("You must have an email")
        if not first_name:
            raise ValueError("You must provide a first name")
        if not last_name:
            raise ValueError("You must provide a last name")
            
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, password, first_name, last_name)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(max_length=155, unique=True)
    username = models.CharField(max_length=100, unique=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = UserManager()

'''