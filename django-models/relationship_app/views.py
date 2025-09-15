from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book  # <-- You need Library imported for the CBV

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library  # <-- Uses Library model
    template_name = "library_detail.html"
    context_object_name = "library"
