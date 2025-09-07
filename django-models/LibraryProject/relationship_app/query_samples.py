import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="George Orwell")
print("Books by George Orwell:", [book.title for book in author.books.all()])

# List all books in a library
library = Library.objects.get(name="Central Library")
print("Books in Central Library:", [book.title for book in library.books.all()])

# Retrieve the librarian for a library
print("Librarian of Central Library:", library.librarian.name)
