from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LibraryListView

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/', views.LibraryListView.as_view(), name='library-list'),
]