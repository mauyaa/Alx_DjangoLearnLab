#!/usr/bin/env python
import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
sys.path.append('.')
django.setup()

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book, UserProfile

def assign_permissions():
    # Create groups
    admin_group, created = Group.objects.get_or_create(name='Admin')
    librarian_group, created = Group.objects.get_or_create(name='Librarian')
    member_group, created = Group.objects.get_or_create(name='Member')

    # Get content type for Book model
    book_ct = ContentType.objects.get_for_model(Book)

    # Get permissions
    can_add_book = Permission.objects.get(codename='can_add_book', content_type=book_ct)
    can_change_book = Permission.objects.get(codename='can_change_book', content_type=book_ct)
    can_delete_book = Permission.objects.get(codename='can_delete_book', content_type=book_ct)

    # Assign permissions to groups
    admin_group.permissions.set([can_add_book, can_change_book, can_delete_book])
    librarian_group.permissions.set([can_add_book, can_change_book])
    member_group.permissions.clear()  # No book permissions for members

    # Assign users to groups based on UserProfile role
    users = User.objects.all()
    for user in users:
        try:
            role = user.userprofile.role
        except UserProfile.DoesNotExist:
            role = 'Member'  # Default role

        # Remove user from all groups first
        user.groups.clear()

        if role == 'Admin':
            user.groups.add(admin_group)
        elif role == 'Librarian':
            user.groups.add(librarian_group)
        elif role == 'Member':
            user.groups.add(member_group)

        user.save()
        print(f"User {user.username} assigned to group {role}")

    print("Permissions and groups assigned successfully!")

if __name__ == "__main__":
    assign_permissions()
