import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import CustomUser
from django.contrib.auth.models import Group

def create_test_users():
    # Create test users
    users_data = [
        {'username': 'editor', 'email': 'editor@example.com', 'password': 'edit123', 'group': 'Editors'},
        {'username': 'viewer', 'email': 'viewer@example.com', 'password': 'view123', 'group': 'Viewers'},
    ]

    for user_data in users_data:
        if not CustomUser.objects.filter(username=user_data['username']).exists():
            user = CustomUser.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password'],
                date_of_birth=date(1995, 5, 5),
            )
            group = Group.objects.get(name=user_data['group'])
            user.groups.add(group)
            print(f"Created user {user.username} in group {user_data['group']}")
        else:
            print(f"User {user_data['username']} already exists.")

if __name__ == "__main__":
    create_test_users()
