from django.db import models
from django.contrib.auth.models import AbstractUser

# ✅ Custom User model
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

# ✅ Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
