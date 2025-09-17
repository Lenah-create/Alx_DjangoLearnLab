```markdown
# Update Book

```python
<<<<<<< HEAD:advanced_features_and_security/update.md
from bookshelf.models import Book

=======
>>>>>>> e9111a16da3f1b89bf08c90f5d93b63769ffb2ec:update.md
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Output: 'Nineteen Eighty-Four'
