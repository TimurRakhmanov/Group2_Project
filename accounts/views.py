from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from . import forms



class AccountCreate(CreateView):
    model = User
    form_class = forms.UserCreationCustomForm
    template_name = "create.html"
    success_url = reverse_lazy("accounts:login")


class AccountLogin(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("accounts:profile")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(redirect_to=reverse_lazy("accounts:login"))


class AccountProfile(TemplateView):
    template_name = "profile.html"  


class AccountUpdate(UpdateView):
    model = User
    fields = ("username", "email",)
    template_name = "update.html"
    success_url = reverse_lazy("accounts:profile")
    

class AccountDelete(DeleteView):
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("accounts:login")