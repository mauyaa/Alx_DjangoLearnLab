# Django Blog

A feature-complete Django blogging platform with authentication, tagging, search, and comment workflows. This project is part of the **Alx_DjangoLearnLab** exercises.

## Features
- User registration, login, logout, and profile editing
- Blog post CRUD with author-only edit/delete permissions
- Comment creation, update, and deletion by comment owners
- Tagging with tag-based filtering and keyword search
- Minimal responsive-friendly styling and reusable base template

## Setup
1. **Clone & enter the project directory**
   ```powershell
   cd C:\Users\USER\Documents\Alx_DjangoLearnLab\django_blog
   ```
2. **Activate the virtual environment**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Apply database migrations**
   ```powershell
   python manage.py migrate
   ```
5. **Run the development server**
   ```powershell
   python manage.py runserver
   ```

## Managing Secrets & Credentials
- Set a strong secret key in your shell (recommended for every non-local deployment):
  ```powershell
  setx DJANGO_SECRET_KEY "your-production-secret"
  ```
- Change the default superuser password before sharing the site:
  ```powershell
  python manage.py changepassword admin
  ```

## Useful Commands
- Create an additional superuser: `python manage.py createsuperuser`
- Load the Django shell: `python manage.py shell`
- Run system checks: `python manage.py check`

## Project Structure Highlights
- `django_blog/` – Django project configuration (settings, URLs, WSGI/ASGI)
- `blog/` – Application logic (models, forms, views, URLs, templates)
- `templates/` – Project-level base template and registration views
- `static/` – Project-level static assets

## Testing Checklist
- Visit `/` to verify post listings
- Use `/register/` or `/accounts/login/` for auth flows
- Create/edit/delete posts at `/posts/...`
- Add and manage comments on post detail pages
- Execute searches via the header search bar and tag chips

## Notes
- SQLite is configured by default; update `DATABASES` in `settings.py` for production-grade databases.
- Collect static files with `python manage.py collectstatic` if preparing for deployment.
