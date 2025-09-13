# TODO List for Advanced Features and Security Implementation

## 1. Custom User Model
- [x] Create CustomUser model in relationship_app/models.py extending AbstractUser with date_of_birth and profile_photo
- [x] Implement CustomUserManager with create_user and create_superuser
- [x] Update UserProfile to reference CustomUser
- [x] Set AUTH_USER_MODEL in settings.py

## 2. Permissions and Groups
- [x] Update Book model permissions to can_view, can_create, can_edit, can_delete
- [x] Update views to use new permission names
- [x] Create groups (Editors, Viewers, Admins) and assign permissions

## 3. Admin Integration
- [x] Create admin.py in relationship_app with CustomUserAdmin

## 4. Security Best Practices
- [x] Update settings.py for security settings (DEBUG=False, XSS filter, etc.)
- [x] Add CSP to INSTALLED_APPS and configure
- [x] Ensure all templates have {% csrf_token %}
- [x] Secure views with proper ORM usage

## 5. HTTPS and Secure Redirects
- [x] Update settings.py for HTTPS settings (SECURE_SSL_REDIRECT, HSTS, etc.)

## 6. Documentation
- [x] Update README.md with setup instructions

## Followup Steps
- [x] Run makemigrations and migrate
- [ ] Create superuser
- [ ] Test permissions and security features
