from django.shortcuts import render
from django.views.generic.edit import CreateView

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from . import forms



class AccountCreate(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "account_create.html"
    success_url = reverse_lazy("accounts:login")


class AccountLogin(LoginView):
    template_name = "account_login.html"


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(redirect_to=reverse_lazy("accounts:login"))


class AccountProfile(TemplateView):
    template_name = "profile.html"  
    