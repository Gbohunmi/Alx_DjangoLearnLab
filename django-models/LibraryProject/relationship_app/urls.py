from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/', views.LibraryListView.as_view(), name='library-list'),
]