from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Post, User, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from taggit.models import Tag

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
    success_url = reverse_lazy('posts')

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
    context_object_name = 'posts'

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


class CommentCreateView(CreateView, LoginRequiredMixin):
    #View for Creating Comments
    model = Comment
    form_class = CommentForm
    template_name = 'blog/create_comment.html'

    def form_valid(self, form):
        # Link the post & author with valid form
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    #View for Editing Comments
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.object.post.pk})



class CommentDeleteView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    #View for Deleting Comments
    model = Comment
    form_class = CommentForm
    template_name = 'blog/delete_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.object.post.pk})
    

def search(request):
    
    query = request.GET.get('q', '')
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        results = Post.objects.none()
    return render(request, 'blog/search.html', {'query': query, 'results': results})

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']  
        tag = Tag.objects.get(slug=tag_slug)  
        return Post.objects.filter(tags=tag)  