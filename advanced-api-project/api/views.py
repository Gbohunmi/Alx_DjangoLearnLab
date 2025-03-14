from django.shortcuts import render
from rest_framework.generics import (ListAPIView, 
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView, 
                                     DestroyAPIView
)
from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class ListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['title', 'year']
    filtering_fields = ['title', 'author', 'year']
    search_fields = ['title', 'author']

class CreateView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateAuthorView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ListAuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer