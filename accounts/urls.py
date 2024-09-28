from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("create/", views.AccountCreate.as_view(), name="account_create"),
]