from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Task 1: List all books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Task 2 (we’ll use this later): full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
