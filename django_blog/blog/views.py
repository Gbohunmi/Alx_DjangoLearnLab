from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post, User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class RegisterView(CreateView):
    # A custom registration view that is class-based and uses UserCreationForm
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/register.html"

# a function-based profile view requiring the user to be logged in
#@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})


class PostCreateView(CreateView):
    #View for creating posts
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostListView(ListView):
    #View for list of all posts
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    #View for details of each post
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'posts'


class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    #View for deleting posts. The mixins implemented are for authentication
    model = Post
    template_name = 'blog/confirm_delete.html'

def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostEditView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
     #View for editing posts. The mixins implemented are for authentication
    model = Post
    template_name = 'blog/edit_post.html'
    context_object_name = 'posts'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


