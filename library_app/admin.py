from django.contrib import admin

from .models import BookList
from .models import Author
from .models import Userprofile
from .models import LoanList


admin.site.site_header = 'Library Management System'


# Register your models here.

#BookList registration
admin.site.register(BookList)

#author registration
admin.site.register(Author)
admin.site.register(Userprofile)
admin.site.register(LoanList)
