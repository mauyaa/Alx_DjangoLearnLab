# TODO: Move CustomUser to bookshelf

- [x] Add CustomUser and CustomUserManager to bookshelf/models.py
- [x] Add CustomUserAdmin to bookshelf/admin.py
- [x] Update settings.py: AUTH_USER_MODEL = 'bookshelf.CustomUser', add MEDIA_ROOT and MEDIA_URL
- [x] Update relationship_app/models.py: import CustomUser from bookshelf
- [x] Update relationship_app/admin.py: import CustomUserAdmin from bookshelf
- [ ] Run makemigrations bookshelf
- [ ] Run migrate
- [ ] Test admin interface for CustomUser
- [ ] Test user creation and profile photo upload
