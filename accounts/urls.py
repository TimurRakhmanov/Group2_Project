from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("create/", views.AccountCreate.as_view(), name="create"),
    path("login/", views.AccountLogin.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", login_required(views.AccountProfile.as_view(), login_url=reverse_lazy("accounts:login")), name="profile"),
]