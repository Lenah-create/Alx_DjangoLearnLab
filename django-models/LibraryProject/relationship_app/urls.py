# relationship_app/urls.py

from django.urls import path
from .views import (
    list_books, 
    LibraryDetailView,
    register_view,
    login_view,
    logout_view
)

urlpatterns = [
    path('books/', list_books, name='list_books'),  # books list
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # library detail
    path('register/', register_view, name='register'),  # user registration
    path('login/', login_view, name='login'),  # user login
    path('logout/', logout_view, name='logout'),  # user logout
]

