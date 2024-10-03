from bs4 import BeautifulSoup
import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()

def api_get_items(item_name):
    request_url = """https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601/"""
    result = requests.get(request_url, params={
        "format": "json", 
        "keyword": item_name, 
        "applicationId": os.getenv("APP_ID"),
        "availability": 1,
        "imageFlag": 1,
        "appointDeliveryDateFlag": 1,
        "elements": "smallImageUrls,mediumImageUrls,itemName,itemPrice,itemUrl,reviewAverage"
        })
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
                "score": item["Item"]["reviewAverage"],
            }
        )
    return main_info
