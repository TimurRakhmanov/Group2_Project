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
    import time
    ingredients, servings = utils.get_ingredients(recipe_id)
    api_data = []
    # imgs, names, prices, urls = [], [], [], 
    for ingredient in ingredients:
        data = utils.get_result(ingredient)
        time.sleep(0.3)
        api_data.extend(data)
    # fetch_data = {ingredient: result for (ingredient, result) in zip(ingredients[:2], api_data)}
    fetch_data = api_data
    return render(request, "ingredients.html", context={"fetch_data": fetch_data, "serving": servings})
