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


class RegisterationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


from django.contrib.auth import views as authentication_views
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Login view
def login_view(request):
    return authentication_views.LoginView.as_view(template_name='relationship_app/login.html')(request)

# Logout view
def logout_view(request):
    return authentication_views.LogoutView.as_view(template_name='relationship_app/logout.html')(request)

def logout_request(request):
  logout(request)
  messages.info(request, "Logged out successfully!")
  return redirect("main:homepage")


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        book = Book(title=title, author_id=author_id)
        book.save()
        return redirect('book_list')  
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author')
        book.save()
        return redirect('book_list')  
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  

    return render(request, 'relationship_app/delete_book.html', {'book': book})