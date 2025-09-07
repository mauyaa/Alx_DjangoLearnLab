from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a queryset for author field to show all authors
        self.fields['author'].queryset = Author.objects.all()
