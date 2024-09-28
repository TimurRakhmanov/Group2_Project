from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from . import forms



class AccountCreate(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "account_create.html"
    success_url = reverse_lazy("accounts:login")


class AccountLogin(LoginView):
    template_name = "account_login.html"
    success_url = reverse_lazy("accounts:create")


class AccountLogout(LogoutView):
    template_name = "account_logout.html"
