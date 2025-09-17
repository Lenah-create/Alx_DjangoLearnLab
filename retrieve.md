```markdown
# Retrieve Book

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)
<<<<<<< HEAD:advanced_features_and_security/retrieve.md
=======
yaml
Copy code
>>>>>>> e9111a16da3f1b89bf08c90f5d93b63769ffb2ec:retrieve.md
