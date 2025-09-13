import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

def create_groups_and_permissions():
    # Define groups and their permissions
    groups_permissions = {
        'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        'Editors': ['can_create', 'can_edit'],
        'Viewers': ['can_view'],
    }

    # Get content type for Book model
    book_content_type = ContentType.objects.get_for_model(Book)

    # Create groups and assign permissions
    for group_name, perms in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        group.permissions.clear()
        for perm_codename in perms:
            try:
                perm = Permission.objects.get(codename=perm_codename, content_type=book_content_type)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                print(f"Permission {perm_codename} not found.")
        group.save()
    print("Groups and permissions have been set up.")

if __name__ == "__main__":
    create_groups_and_permissions()
