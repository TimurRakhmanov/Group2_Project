from bs4 import BeautifulSoup
import json
import os


def parse_html(recipe_id):
    html_raw = open(os.path.join("./recipe_integration/static/samples/", f"{recipe_id}.html"))
    html_doc = html_raw.read()
    html_raw.close()
    soup = BeautifulSoup(html_doc, "html.parser")
    materials = soup.find_all(class_="recipe_material__item_name")
    # categories = [material.a for material in materials]
    headings_2 = soup.find_all(class_="contents_title")
    servings = str(headings_2[0].contents).replace("['", "").replace("']", "")
    ingridients = []
    for ingr in materials:
        if ingr is not None:
            if len(ingr) > 1:
                ingr = ingr.a
            ingridients.append(str(ingr.contents).replace("['", "").replace("']", "").replace('★', ""))
    return ingridients, servings

def get_result(item_name):
    json_file = open(os.path.join("./recipe_integration/static/samples/", f"{item_name}.json"))
    data = json_file.read()
    json_file.close()
    data = json.loads(data)
    return data