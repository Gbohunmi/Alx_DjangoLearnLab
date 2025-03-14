from django.db import models

# Create your models here.


#Defined the Author Model 
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
           return self.name
    
    class Meta:
        app_label = 'api'

#Defined the Book Model with author foreign key linked to the Author Model
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')