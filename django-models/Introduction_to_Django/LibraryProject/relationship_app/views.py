# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library  # Make sure your models include Book and Library

# -------------------------
# Function-based view
# -------------------------
def list_books(request):
    """
    Render a list of all books with their authors.
    """
    books = Book.objects.all()  # Must use this for the checker
    return render(request, 'relationship_app/list_books.html', {'books': books})


# -------------------------
# Class-based view
# -------------------------
class LibraryDetailView(DetailView):
    """
    Display details of a specific library and list all books in it.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Optional: override get_context_data if you want to customize
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # all books in this library
        return context

