from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from . import views

app_name = "accounts"
urlpatterns = [
    path("create/", views.AccountCreate.as_view(), name="create"),
    path("login/", views.AccountLogin.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", login_required(views.AccountProfile.as_view(), login_url=reverse_lazy("accounts:login")), name="profile"),
    path("update/<int:pk>/", login_required(views.AccountUpdate.as_view()), name="update"),
    path("delete/<int:pk>/", login_required(views.AccountDelete.as_view()), name="delete"),
]