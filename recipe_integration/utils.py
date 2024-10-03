from bs4 import BeautifulSoup
import json
import os


# def parse_html(recipe_id):
#     html_raw = open(os.path.join("./recipe_integration/static/samples/", f"{recipe_id}.html"))
#     html_doc = html_raw.read()
#     html_raw.close()
#     soup = BeautifulSoup(html_doc, "html.parser")
#     materials = soup.find_all(class_="recipe_material__item_name")
#     # categories = [material.a for material in materials]
#     headings_2 = soup.find_all(class_="contents_title")
#     servings = str(headings_2[0].contents).replace("['", "").replace("']", "")
#     ingridients = []
#     for ingr in materials:
#         if ingr is not None:
#             if len(ingr) > 1:
#                 ingr = ingr.a
#             ingridients.append(str(ingr.contents).replace("['", "").replace("']", "").replace('★', ""))
#     return ingridients, servings


def get_ingredients(recipe_id):
    with open(os.path.join("./recipe_integration/static/samples/", f"{recipe_id}.json"), mode="r") as f:
        json_data = f.read()
    data = json.loads(json_data)
    return data["Ingredients"], data["Servings"]

def get_result(item_name):
    fname = os.path.join("./recipe_integration/static/samples/", f"{item_name}.json")
    with open(fname, mode="r") as f:
        json_file = f.read()
    data = json.loads(json_file)
    items = data["Items"]
    # item_name = data["Items"][0]["Item"]["itemName"]
    # print(items[0]["Item"]["smallImageUrls"][0])
    main_info = []
    for item in items:
        main_info.append(
            {
                "product_name": item_name,
                "img": item["Item"]["mediumImageUrls"][0]["imageUrl"],
                "name": item["Item"]["itemName"],
                "price": item["Item"]["itemPrice"],
                "url": item["Item"]["itemUrl"],

            }
        )
    # imgs = [img["Item"]["mediumImageUrls"][0]["imageUrl"] for img in items]
    # names = [item["Item"]["itemName"] for item in items]
    # prices = [item["Item"]["itemPrice"] for item in items]
    # urls = [item["Item"]["itemUrl"] for item in items]
    # main_info = {
    #     "product_name": item_name,
    #     "imgs": imgs,
    #     "names": names,
    #     "prices": prices, 
    #     "urls": urls,
    # }
    return main_info
