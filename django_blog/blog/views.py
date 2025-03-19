from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post, User
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
# Create your views here.

class RegisterView(CreateView):
    # A custom registration view that is class-based and uses UserCreationForm
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/registration.html"

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




