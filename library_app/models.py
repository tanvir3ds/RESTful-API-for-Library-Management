from django.db import models
from django.contrib.auth.models import User

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


class LoanList(models.Model):
    book= models.ManyToManyField(BookList, null=True, blank=True)
    user= models.ManyToManyField(User, null=True, blank=True)

