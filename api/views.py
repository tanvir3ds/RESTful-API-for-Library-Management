from rest_framework import generics, permissions

from library_app.models import BookList
from library_app.models import Author
from django.contrib.auth.models import User


from .serializers import BookListSerializer
from .serializers import AuthorSerializer
from .serializers import UserSerializer


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
    queryset = BookList.objects.all().order_by('-id')[:1] # latest 
    serializer_class = BookListSerializer





class AuthorsAPINewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Author.objects.all().order_by('-id')[:1] # latest 
    serializer_class = AuthorSerializer




class UserAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all().order_by('-id') # latest 
    serializer_class = UserSerializer



class UserAPIDetailView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all().order_by('-id')[:1] # latest 
    serializer_class = UserSerializer

