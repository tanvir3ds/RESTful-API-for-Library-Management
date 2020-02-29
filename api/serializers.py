from rest_framework import serializers

from library_app.models import BookList

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList 
        
        fields = ('__all__')
        #fields = ['title']
        