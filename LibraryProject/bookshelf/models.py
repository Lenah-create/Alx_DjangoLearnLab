from django.db import models
<<<<<<< HEAD:advanced_features_and_security/bookshelf/models.py
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
from django.contrib.auth.models import UserManager, BaseUserManager
# Create your models here.
# class UserProfile(models.Model):

class CustomUser(AbstractUser):

    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    objects = CustomUserManager()
    def __str__(self):
        return self.username

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(null=True, blank=True)

    class Meta:
        permissions = (
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        )

    def __str__(self):
        return self.title
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user(username, email, password, **extra_fields)
=======
from django.conf import settings

# ------------------------
# Author Model
# ------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# ------------------------
# Book Model with Permissions
# ------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="bookshelf_books"
    )

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author.name}"


# ------------------------
# Library Model
# ------------------------
class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


# ------------------------
# Librarian Model
# ------------------------
class Librarian(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookshelf_librarian"  # unique reverse accessor
    )
    library = models.OneToOneField('Library', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
>>>>>>> e9111a16da3f1b89bf08c90f5d93b63769ffb2ec:bookshelf/models.py
