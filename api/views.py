<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer # type: ignore

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet): # type: ignore
    queryset = Book.objects.all()
    serializer_class = BookSerializer
>>>>>>> f89c1f1 (Fixed nested Git repo and added advanced-api-project files)
