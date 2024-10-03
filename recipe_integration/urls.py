from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "recipe_int"
urlpatterns = [
    path("recipe/", login_required(views.main), name="main"),
    path("recipe/fetch/<int:recipe_id>", login_required(views.recipe_fetch), name="recipe_fetch"),
]