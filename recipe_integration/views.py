from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from . import forms, utils


def main(request):
    if request.method == "POST":
        form = forms.RecipeFeatchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"fetch/{form.cleaned_data['recipe_id']}")
    else:
        form = forms.RecipeFeatchForm()
        return render(request, "main.html", {"form": form})


def recipe_fetch(request, recipe_id):
    ingredients, servings = utils.get_ingredients(recipe_id)
    api_data = []
    # imgs, names, prices, urls = [], [], [], 
    for ingridient in ingredients[:2]:
        data = utils.get_result(ingridient)
        api_data.extend(data)
    # fetch_data = {ingridient: result for (ingridient, result) in zip(ingredients[:2], api_data)}
    fetch_data = api_data
    return render(request, "ingredients.html", context={"fetch_data": fetch_data, "serving": servings})
