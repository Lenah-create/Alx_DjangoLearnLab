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

