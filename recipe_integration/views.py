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
    ingridients, servings = utils.parse_html(recipe_id)
    return render(request, "ingridients.html", context={"ingridients": ingridients, "serving": servings})

    
