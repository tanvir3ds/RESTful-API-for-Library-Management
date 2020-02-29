from rest_framework import generics

from library_app.models import BookList
from library_app.models import Author


from .serializers import BookListSerializer
from .serializers import AuthorSerializer

class BooksAPIView(generics.ListAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer

class AuthorsAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

