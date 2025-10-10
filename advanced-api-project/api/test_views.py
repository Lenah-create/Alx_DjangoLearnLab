from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):
    """
    ✅ Unit tests for the Book API endpoints
    Covers CRUD, permissions, filtering, searching, and ordering.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2021)

        # Define URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book2.pk})

    # --- List View ---
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # --- Retrieve View ---
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # --- Create View (Authenticated) ---
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {"title": "Created Book", "author": "Author X", "publication_year": 2024}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(title="Created Book").exists())

    # --- Create View (Unauthenticated) ---
    def test_create_book_unauthenticated(self):
        data = {"title": "Unauthorized", "author": "Anon", "publication_year": 2024}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- Update View ---
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {"title": "Updated Title", "author": "Author Y", "publication_year": 2020}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # --- Delete View ---
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    # --- Permissions ---
    def test_unauthenticated_user_cannot_delete(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- Filtering ---
    def test_filter_books_by_author(self):
        url = f"{self.list_url}?author=Author A"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all("Author A" in book['author'] for book in response.data))

    # --- Searching ---
    def test_search_books(self):
        url = f"{self.list_url}?search=Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # --- Ordering ---
    def test_order_books_by_publication_year(self):
        url = f"{self.list_url}?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
