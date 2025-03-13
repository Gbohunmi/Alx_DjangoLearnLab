from django.shortcuts import render
from rest_framework.generics import (ListAPIView, 
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView, 
                                     DestroyAPIView
)
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
# Create your views here.

class ListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateAuthorView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer