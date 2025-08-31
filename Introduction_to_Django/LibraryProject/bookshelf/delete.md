 GNU nano 8.4                  bookshelf/delete.md
```markdown
# Delete Book

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: <QuerySet []>


