# Permissions and Groups Setup

This document explains how permissions and groups are configured and used in the Django application.

## Custom Permissions

The `Book` model in `relationship_app/models.py` defines the following custom permissions:

- `can_view`: Permission to view book instances.
- `can_create`: Permission to create new book instances.
- `can_edit`: Permission to edit existing book instances.
- `can_delete`: Permission to delete book instances.

## Groups and Assigned Permissions

Three groups are created with the following permissions:

- **Admins**: `can_view`, `can_create`, `can_edit`, `can_delete`
- **Editors**: `can_create`, `can_edit`
- **Viewers**: `can_view`

Groups and permissions are created and assigned using the script `LibraryProject/assign_permissions.py`.

## Usage in Views

Views that create, edit, or delete books are protected using the `@permission_required` decorator with the appropriate permission codename, for example:

```python
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...
```

## Creating Test Users

Test users are created and assigned to groups using the script `LibraryProject/create_test_users.py`.

## Security Best Practices

- `DEBUG` is set to `False` for production.
- Security settings such as `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, and `SECURE_CONTENT_TYPE_NOSNIFF` are enabled.
- CSRF and session cookies are configured to be secure in production (`CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`).
- Content Security Policy (CSP) is enforced using the `csp` app and middleware.

## HTTPS Configuration

- HTTPS redirects and HSTS settings are configured in `settings.py`.
- For development, secure cookie flags and SSL redirect are disabled to avoid issues.
- In production, enable `SECURE_SSL_REDIRECT`, `CSRF_COOKIE_SECURE`, and `SESSION_COOKIE_SECURE`.

## Notes

- Ensure all forms include `{% csrf_token %}` in templates to protect against CSRF attacks.
- Use Django ORM and form validation to prevent SQL injection.
- Review deployment environment to properly configure SSL/TLS certificates.
