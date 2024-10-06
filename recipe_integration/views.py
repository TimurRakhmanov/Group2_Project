from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from . import forms, utils



def main(request):
    if request.method == "POST":
        form = forms.RecipeFetchForm(request.POST)
        # Validate the input first before the redirect
        if form.is_valid():
            return HttpResponseRedirect(f"fetch/{form.cleaned_data['recipe_id']}")
    else:
        form = forms.RecipeFetchForm()
        return render(request, "main.html", {"form": form})


def recipe_fetch(request, recipe_id):
    name, servings, ingredients, amount = utils.get_ingredients(recipe_id)
    api_data = []
    # Store the ingredient and its corresponding amoun in the dictionary
    ingredients = {ingredient: amount for (ingredient, amount) in zip(ingredients, amount)}
    # Iterate over the dictionary to get the correct data from API
    for ingredient, amount in ingredients.items():
        data = utils.get_result(item_name=ingredient, item_amount=amount, recipe_id=recipe_id, local_cache=True)
        api_data.extend(data)
    return render(request, "ingredients.html", context={"fetch_data": api_data, "serving": servings, "name": name,})
