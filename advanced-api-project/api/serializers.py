from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

#Defined Book Serializer and validated the Publication year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','publication_year','author']

    def validate_publication_year(self, publication_year):

        now = int(datetime.now().year)
        if now < (publication_year):
            raise serializers.ValidationError(f'{publication_year} is in the future')
        return super().validate(publication_year)

#Defined Author Serializer and nested BookSerializer in it to return book data
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:    
        model = Author
        fields = ['name', 'books']