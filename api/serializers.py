from rest_framework import serializers

from library_app.models import BookList
from library_app.models import Author
from django.contrib.auth.models import User


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList 
        
        fields = ('__all__')
        

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author 
        
        fields = ('__all__')
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        
        fields = ('__all__')
        

    