from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from . import forms

from bs4 import BeautifulSoup

import os

def main(request):
    if request.method == "POST":
        form = forms.RecipeFeatchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(f"fetch/{form.cleaned_data['recipe_id']}")
    else:
        form = forms.RecipeFeatchForm()
        return render(request, "main.html", {"form": form})


def recipe_fetch(request, recipe_id):
    html_raw = open(os.path.join("./recipe_integration/static/samples/", f"{recipe_id}.html"))
    html_doc = html_raw.read()
    html_raw.close()
    soup = BeautifulSoup(html_doc, "html.parser")
    materials = soup.find_all(class_="recipe_material__item_name")
    # materials.find_all(class_="recipe_material__item_name")
    categories = [material.a for material in materials]
    ingridients = []
    for ingr in materials:
        if ingr is not None:
            if len(ingr) > 1:
                # ing_line = ingr[1]
                ingr = ingr.a
            ingridients.append(str(ingr.contents).replace("['", "").replace("']", "").replace('★', ""))
    return render(request, "ingridients.html", context={"ingridients": ingridients})

    
