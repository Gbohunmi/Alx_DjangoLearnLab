from django.urls import path
from .views import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    CreateAuthorView
)

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView .as_view(), name='book-details'),
    path('books/create', CreateView.as_view(), name='create-book'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='update-book'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='delete-book'),
    path('books/create-author', CreateAuthorView.as_view(), name='create-author'),
    
]
