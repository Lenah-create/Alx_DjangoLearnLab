from django.db import models

<<<<<<< HEAD
class Author(models.Model):
    """
    Author model to store writer information.
    An Author can have multiple Books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model representing a written work.
    Each Book is linked to one Author via a foreign key.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
=======
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"
>>>>>>> f89c1f1 (Fixed nested Git repo and added advanced-api-project files)
