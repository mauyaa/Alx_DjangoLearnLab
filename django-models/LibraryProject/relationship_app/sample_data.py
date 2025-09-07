from .models import Author, Book, Library, Librarian, UserProfile
from django.contrib.auth.models import User

def create_sample_data():
    # Create sample authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")
    author3 = Author.objects.create(name="Agatha Christie")

    # Create sample books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1, publication_year=1997)
    book2 = Book.objects.create(title="A Game of Thrones", author=author2, publication_year=1996)
    book3 = Book.objects.create(title="Murder on the Orient Express", author=author3, publication_year=1934)
    book4 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1, publication_year=1998)

    # Create sample library
    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2, book3, book4)

    # Create sample librarian
    librarian1 = Librarian.objects.create(name="John Smith", library=library1)

    # Create sample users with different roles
    admin_user = User.objects.create_user(username='admin', password='admin123')
    librarian_user = User.objects.create_user(username='librarian', password='lib123')
    member_user = User.objects.create_user(username='member', password='mem123')

    # Create user profiles
    UserProfile.objects.create(user=admin_user, role='Admin')
    UserProfile.objects.create(user=librarian_user, role='Librarian')
    UserProfile.objects.create(user=member_user, role='Member')

    print("Sample data created successfully!")

if __name__ == "__main__":
    create_sample_data()
