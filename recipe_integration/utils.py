from bs4 import BeautifulSoup
import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()
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

def api_get_items(item_name):
    request_url = """https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601/"""
    result = requests.get(request_url, params={"format": "json", "keyword": item_name, "applicationId": os.getenv("APP_ID")})
    return result


def get_ingredients(recipe_id):
    with open(os.path.join("./recipe_integration/static/samples/", f"{recipe_id}.json"), mode="r") as f:
        json_data = f.read()
    data = json.loads(json_data)
    return data["Ingredients"], data["Servings"]

def get_result(item_name):
    api_result = api_get_items(item_name)
    data = api_result.json()
    items = data["Items"]
    main_info = []
    for item in items:
        main_info.append(
            {
                "product_name": item_name,
                "img": item["Item"]["smallImageUrls"][0]["imageUrl"],
                "name": item["Item"]["itemName"],
                "price": item["Item"]["itemPrice"],
                "url": item["Item"]["itemUrl"],

            }
        )
    return main_info
