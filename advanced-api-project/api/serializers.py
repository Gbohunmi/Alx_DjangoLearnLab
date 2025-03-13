from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

#Defined Book Serializer and validated the Publication year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['__all__']

    def validate(self, publication_year):
        if datetime.now().year < publication_year:
            raise serializers.ValidationError(f'{publication_year} is in the future')
        return super().validate(publication_year)

#Defined Author Serializer and nested BookSerializer in it to return book data
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:    
        model = Author
        fields = ['id','name', 'books']