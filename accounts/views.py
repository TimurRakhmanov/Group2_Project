from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from . import forms



class AccountCreate(CreateView):
    model = User
    form_class = forms.AccountCreateForm
    template_name = "account_create.html"
