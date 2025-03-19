from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import RegisterView, profile_update
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path("home/", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path('profile/', views.profile_update, name='profile'),

]