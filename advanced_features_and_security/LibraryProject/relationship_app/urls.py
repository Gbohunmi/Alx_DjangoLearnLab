from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LibraryListView
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='books'),
    path('library/', views.LibraryListView.as_view(), name='library-list'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", auth_views.register, name="register"),
    path("admin/", views.admin_view, name="admin-view"),
    path("librarian/", views.librarian_view, name="librarian-view"),
    path("member/", views.member_view, name="member-view"),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]

#path("login/", auth_views.LoginView.as_view(template_name="login.html'), name="login"),
#path("logout/", auth_views."LogoutView.as_view(template_name="logout.html'), name="logout"),