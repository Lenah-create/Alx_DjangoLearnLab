from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required

from .models import Book
from .models import Library 
from .forms import BookForm # pyright: ignore[reportMissingImports]

# -------------------------
# Function-based view: list all books
# -------------------------
@permission_required('relationship_app.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# -------------------------
# Class-based view: show details of a specific library, including its books
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# -------------------------
# User Authentication Views
# -------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# -------------------------
# Custom Permissions Views: Add, Edit, Delete Books
# -------------------------
@permission_required('relationship_app.can_create', raise_exception=True)
def add_book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})


@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form})


@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, "relationship_app/delete_book.html", {"book": book})
