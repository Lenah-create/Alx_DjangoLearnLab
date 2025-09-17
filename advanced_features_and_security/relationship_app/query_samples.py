import os
import sys
import django

# Add project directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# Setup Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ---- Seed data (only if DB is empty) ----
def seed_data():
    if not Author.objects.exists():
        author1 = Author.objects.create(name="John Doe")
        author2 = Author.objects.create(name="Jane Smith")

        book1 = Book.objects.create(title="Django for Beginners", author=author1)
        book2 = Book.objects.create(title="Advanced Django", author=author1)
        book3 = Book.objects.create(title="Python Mastery", author=author2)

        library = Library.objects.create(name="Central Library")
        library.books.add(book1, book2, book3)

        Librarian.objects.create(name="Alice", library=library)
        print("✅ Sample data created.")
    else:
        print("ℹ️ Sample data already exists.")

# ---- Queries ----
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

if __name__ == "__main__":
    seed_data()
    print("Books by John Doe:", list(get_books_by_author("John Doe")))
    print("Books in Central Library:", list(get_books_in_library("Central Library")))
    print("Librarian of Central Library:", get_librarian_for_library("Central Library"))

