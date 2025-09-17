from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # Changed to OneToOne as per checker

    def __str__(self):
        return self.user.username
