from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import (LogoutView, LoginView)
from django.urls import reverse_lazy
from .forms import UserCreationForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


class LoginView(LoginView):
    # redirect_authenticated_user = True
    redirect_field_name = 'home'
    template_name = 'login.html'


class LogoutView(LogoutView):
    next_page = 'home'