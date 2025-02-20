from django.shortcuts import render
from .models import Book, Library
from django.views.generic import  ListView
from django.urls import reverse_lazy
# Create your views here.

def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'books/list_books.html', context)

class LibraryListView(ListView):
  """A class-based view for updating details of a specific book."""
  model = Library
  template_name = 'books/library_detail.html'
  context_object_name = 'library'