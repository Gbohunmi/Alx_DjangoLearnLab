from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import  ListView

from django.views.generic import DetailView
from django.views.generic.detail import DetailView
# Create your views here.

def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)

class LibraryListView(ListView):
  """A class-based view for updating details of a specific book."""
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = 'library'

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'