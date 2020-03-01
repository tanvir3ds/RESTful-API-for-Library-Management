from django.urls import path

from . views import BooksAPIView
from . views import AuthorsAPIView
from . views import BooksAPIDetailView
from . views import BooksAPINewView
from . views import AuthorsAPINewView



urlpatterns = [

    path('books/', BooksAPIView.as_view()),
    path('authors/', AuthorsAPIView.as_view()),
    path('books/<int:pk>/', BooksAPIDetailView.as_view()),
    path('books/new/', BooksAPINewView.as_view()),
    path('authors/new/', AuthorsAPINewView.as_view()),
]