from rest_framework import generics

from library_app.models import BookList


from .serializers import BookListSerializer

class BooksAPIView(generics.ListAPIView):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer

