from django.contrib import admin
from .models import Book, Library, Librarian, UserProfile
# Register your models
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
