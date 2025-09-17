## Permissions and Groups Setup

- Custom permissions defined in `Book` model:
  - can_view
  - can_create
  - can_edit
  - can_delete

- Groups:
  - Viewers → can_view
  - Editors → can_view, can_create, can_edit
  - Admins → all permissions

- Views are protected with `@permission_required` decorators in `bookshelf/views.py`.
