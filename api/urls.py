from django.urls import path

from . views import BooksAPIView
from . views import AuthorsAPIView

urlpatterns = [

    path('books/', BooksAPIView.as_view()),
    path('authors/', AuthorsAPIView.as_view()),
]