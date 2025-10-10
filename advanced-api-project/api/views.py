from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# 🔹 Anyone can view (read-only) — with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Added functionality
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # filtering
    search_fields = ['title', 'author']  # searching
    ordering_fields = ['title', 'publication_year']  # ordering


# 🔹 Anyone can view details (read-only)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# 🔹 Only authenticated users can create
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# 🔹 Only authenticated users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# 🔹 Only authenticated users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
