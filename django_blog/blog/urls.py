from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import RegisterView, PostCreateView, PostListView, CommentCreateView, CommentUpdateView, CommentDeleteView, PostDeleteView, PostDetailView, PostEditView
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
    path("post/new/", PostCreateView.as_view(), name="create-post"),
    path("posts", PostListView.as_view(), name="posts"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-details"),
    path("post/<int:pk>/update/", PostEditView.as_view(), name="edit-post"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete-post"),

    #Comment Views
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="create-comment"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="edit-comment"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"),

]