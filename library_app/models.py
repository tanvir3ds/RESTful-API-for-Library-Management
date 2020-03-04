from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BookList(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='book_picture')
    price= models.IntegerField()
    quantity= models.IntegerField()
    


    Book_Author= models.ForeignKey(
        'Author',
        on_delete=models.CASCADE

        )
    def __str__(self):
        return self.title   



class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile',blank=True)

    def __str__(self):
        return self.user.username  

class BookLoan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    Book = models.ForeignKey(BookList, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    
    Accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.Book.title 


