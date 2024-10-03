from bs4 import BeautifulSoup
import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()

def save_api_response(item_name, recipe_id):
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
    result = result.json()
    with open(os.path.join(f"./recipe_integration/static/samples/api_responses/{recipe_id}/", f"{item_name}.json"), mode="w") as f:
        json.dump(result, f)


def get_api_response(item_name, recipe_id):
    with open(os.path.join(f"./recipe_integration/static/samples/api_responses/{recipe_id}/", f"{item_name}.json"), mode="r") as f:
        data = json.loads(f.read())
    return data


def get_ingredients(recipe_id):
    with open(os.path.join(f".{os.path.sep}recipe_integration{os.path.sep}static{os.path.sep}samples{os.path.sep}recipes{os.path.sep}", f"{recipe_id}.json"), mode="r", encoding="utf-8_sig") as f:

        json_data = f.read()
    data = json.loads(json_data)
    return data["Name"], data["Servings"], data["Ingredients"], data["Amount"]

def get_result(item_name, item_amount, recipe_id):
    # save_api_response(item_name, recipe_id)
    api_result = get_api_response(item_name, recipe_id)
    data = api_result
    items = data["Items"]
    main_info = []
    for item in items[:10]:
        main_info.append(
            {
                "product_name": item_name,
                "product_amount": item_amount,
                "img": item["Item"]["smallImageUrls"][0]["imageUrl"],
                "name": item["Item"]["itemName"],
                "price": item["Item"]["itemPrice"],
                "url": item["Item"]["itemUrl"],
                "score": item["Item"]["reviewAverage"],
            }
        )
    return main_info
