<<<<<<< HEAD:advanced_features_and_security/README.md
Permissions
Models(bookshefl/models.py)
Custom Permissions Book Model

can_view: Allows viewing of a book instance.
can_create: Allows creation of a new book instance.
can_edit: Allows editing of an existing book instance.
can_delete: Allows deletion of a book instance.
Views
Views check if user has permission to carry out action, If they do not they are served an error

Groups
Viewers: Have can_view permission.
Editors: Have can_create and can_edit permissions.
Admins: Have all four permissions (can_view, can_create, can_edit, can_delete).
=======
# Alx_DjangoLearnLab

## Project: Django Models & Views Practice

This project demonstrates the use of Django's ORM relationships and view types. It includes:

- **Models with relationships:**
  - `Author` (name)
  - `Book` (title, ForeignKey to Author)
  - `Library` (name, ManyToMany with Book)
  - `Librarian` (name, OneToOne with Library)
- **Views:**
  - Function-Based View: list all books (`list_books`)
  - Class-Based View: show library details (`LibraryDetailView`)
- **Templates:**
  - `list_books.html` — displays all books and authors
  - `library_detail.html` — displays a specific library and its books

## Project Structure

>>>>>>> e9111a16da3f1b89bf08c90f5d93b63769ffb2ec:README.md
