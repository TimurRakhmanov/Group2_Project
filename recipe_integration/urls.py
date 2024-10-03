from django.urls import path
from . import views

app_name = "recipe_int"
urlpatterns = [
    path("recipe/", views.main, name="main"),
    path("recipe/fetch/<int:recipe_id>", views.recipe_fetch, name="recipe_fetch"),
]