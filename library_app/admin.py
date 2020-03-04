from django.contrib import admin

from .models import BookList
from .models import Author
from .models import Userprofile, BookLoan
#from .models import LoanList


admin.site.site_header = 'Library Management System'


# Register your models here.

#BookList registration
admin.site.register(BookList)

#author registration
admin.site.register(Author)
admin.site.register(Userprofile)

#admin.site.register(LoanList)
class BookLoanDetailsView(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered_date',
        'Accepted',
        'Book',
        'quantity',
    
    ]
admin.site.register(BookLoan, BookLoanDetailsView)
