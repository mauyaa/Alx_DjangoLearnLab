# 📚 LibraryProject (Django) - Advanced Features and Security

This Django project demonstrates advanced user management, permissions, groups, and security best practices for a library application.

---

## 🚀 Features

### Custom User Model
- Extended Django's `AbstractUser` with additional fields:
  - `date_of_birth` (DateField)
  - `profile_photo` (ImageField)
- Custom user manager for handling user creation
- Configured as `AUTH_USER_MODEL` in settings

### Permissions and Groups
- Custom permissions on Book model: `can_view`, `can_create`, `can_edit`, `can_delete`
- User groups: Admins, Editors, Viewers
- Permission-based access control in views using `@permission_required` decorators

### Admin Integration
- Custom admin interface for managing users, books, and other models
- Enhanced admin for CustomUser with additional fields

### Security Best Practices
- DEBUG set to False for production
- XSS protection: SECURE_BROWSER_XSS_FILTER enabled
- Clickjacking protection: X_FRAME_OPTIONS set to 'DENY'
- Content type sniffing prevention: SECURE_CONTENT_TYPE_NOSNIFF enabled
- Secure cookies: CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE enabled
- CSRF tokens in all forms
- Content Security Policy (CSP) configured to reduce XSS risks

### HTTPS and Secure Redirects
- SECURE_SSL_REDIRECT: Redirects all HTTP requests to HTTPS
- HSTS: SECURE_HSTS_SECONDS set to 1 year, includes subdomains and preload
- Secure cookie settings for production

### Apps
- `bookshelf`: Basic book management
- `relationship_app`: Advanced user profiles, books with permissions, libraries, librarians

---

## 📂 Project Structure
LibraryProject/
│── LibraryProject/ # Main project settings
│── bookshelf/ # Basic book app
│── relationship_app/ # Advanced app with custom user, permissions
│── db.sqlite3 # SQLite database
│── manage.py # Django management script
│── assign_permissions.py # Script to set up groups and permissions
│── TODO.md # Implementation checklist
│── README.md # This file

---

## ⚙️ Setup and Installation

1. Install dependencies:
   ```bash
   pip install django django-csp Pillow
   ```

2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Set up groups and permissions:
   ```bash
   python assign_permissions.py
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

6. Access the application:
   - Admin: http://127.0.0.1:8000/admin/
   - Book list: http://127.0.0.1:8000/relationship_app/books/

---

## 🔐 Permissions and Groups Setup

- **Admins**: Full access (view, create, edit, delete books)
- **Editors**: Create and edit books
- **Viewers**: View books only

Assign users to groups via Django admin or programmatically.

---

## 🛡️ Security Configuration

- All security settings are configured in `LibraryProject/settings.py`
- CSP headers prevent XSS by restricting resource loading
- HTTPS settings ensure secure communication
- CSRF protection on all forms

For production deployment:
- Set `DEBUG = False`
- Configure web server (e.g., Nginx) for SSL/TLS
- Update `ALLOWED_HOSTS` and `SECRET_KEY`

---

## 📝 Testing Permissions

1. Create test users and assign to groups
2. Log in as each user type
3. Attempt to access restricted views (e.g., add/edit/delete books)
4. Verify that permissions are enforced correctly

---

## 👨‍💻 Author
Project enhanced with advanced features and security
