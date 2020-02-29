from django.contrib import admin

from .models import BookList
from .models import Author


# Register your models here.

#BookList registration
admin.site.register(BookList)

#author registration
admin.site.register(Author)