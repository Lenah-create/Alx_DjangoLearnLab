# Create Book

```python
from bookshelf.models import Book

<<<<<<< HEAD:advanced_features_and_security/create.md
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>
=======
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# Output: <Book: 1984 by George Orwell (1949)>

>>>>>>> e9111a16da3f1b89bf08c90f5d93b63769ffb2ec:create.md
