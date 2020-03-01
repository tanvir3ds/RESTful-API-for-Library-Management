from rest_framework import generics, permissions

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




class BooksAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer

class BooksAPINewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = BookList.objects.all().order_by('-id')[:1] # latest quote
    serializer_class = BookListSerializer





class AuthorsAPINewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Author.objects.all().order_by('-id')[:1] # latest quote
    serializer_class = AuthorSerializer

