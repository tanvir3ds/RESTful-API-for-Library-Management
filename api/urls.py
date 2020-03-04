from django.urls import path

from . views import BooksAPIView
from . views import AuthorsAPIView
from . views import BooksAPIDetailView
from . views import BooksAPINewView
from . views import AuthorsAPINewView
from . views import UserAPIView
from . views import UserAPIDetailView
from . views import LoanBooksAPIView
from . views import LoanBooksAPINewView




urlpatterns = [

    path('books/', BooksAPIView.as_view()),
    path('authors/', AuthorsAPIView.as_view()),
    path('books/<int:pk>/', BooksAPIDetailView.as_view()),
    path('books/new/', BooksAPINewView.as_view()),
    path('authors/new/', AuthorsAPINewView.as_view()),
    
    path('user/', UserAPIView.as_view()),
    path('user/<int:pk>/', UserAPIDetailView.as_view()),


    path('loanbooks/', LoanBooksAPIView.as_view()),
    path('loanbooks/new/', LoanBooksAPINewView.as_view()),



]