from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import RegisterView, PostCreateView,PostListView
from . import views

urlpatterns = [
    #Login & Logout Views
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    
    #Register and Profile edit views
    path("register/", RegisterView.as_view(template_name="register.html"), name="register"),
    path('profile/', views.profile_update, name='profile'),
    
    #Home Views
    path("home/", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),

    #Post Views
    path("post/new/", PostCreateView.as_view(template_name="post_form.html"), name="create-post"),
    path("posts", PostListView.as_view(template_name="post_list.html"), name="posts"),
    path("post/<int:pk>", PostCreateView.as_view(template_name="post_detail.html"), name="post-details"),
    path("/post/<int:pk>/update/", PostCreateView.as_view(template_name="edit_post.html"), name="edit-post"),
    path("/post/<int:pk>/delete/", PostCreateView.as_view(template_name="confirm_delete.html"), name="delete-post"),
]