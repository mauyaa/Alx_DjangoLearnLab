import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import CustomUser

def create_superuser():
    if not CustomUser.objects.filter(username='admin').exists():
        user = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            date_of_birth=date(1990, 1, 1),  # Example date
            # profile_photo can be None for now
        )
        print("Superuser created: admin / admin123")
    else:
        print("Superuser already exists.")

if __name__ == "__main__":
    create_superuser()
