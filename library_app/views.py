from django.shortcuts import render, redirect, HttpResponse

# import model
from . models import Author
from . models import BookList

# Create your views here.

def home(request):
    return render(request, 'login.html' )


def registration(request):
    return render(request, 'registration.html' )

def library(request):
    booklists = BookList.objects.all()

    return render(request, 'library.html', {'booklists':booklists,} )
