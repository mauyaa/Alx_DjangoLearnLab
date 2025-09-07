#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
sys.path.append('.')
django.setup()

from django.contrib.auth.models import User
from relationship_app.models import UserProfile

def fix_user_profiles():
    users = User.objects.all()
    print("Existing users and their profiles:")

    for user in users:
        has_profile = hasattr(user, 'userprofile')
        print(f"{user.username}: has_profile={has_profile}")

        if not has_profile:
            # Create profile for user without one
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={'role': 'Member'}
            )
            if created:
                print(f"  -> Created profile for {user.username} with role 'Member'")
            else:
                print(f"  -> Profile already exists for {user.username}")

    print("\nAll users now have profiles!")

if __name__ == "__main__":
    fix_user_profiles()
