from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LibraryListView
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/', views.LibraryListView.as_view(), name='library-list'),
    path("login/", auth_views.LoginView.as_view(template_name = 'login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = 'logout.html'), name="logout"),
    path("register/", auth_views.register, name="register") 
]