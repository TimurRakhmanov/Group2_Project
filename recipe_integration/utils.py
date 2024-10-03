from bs4 import BeautifulSoup
import json
import os
import requests

from dotenv import load_dotenv

load_dotenv()

def get_api_response(item_name, recipe_id, save=False):
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
    if save:
        try:
            with open(os.path.join(f"./recipe_integration/static/samples/api_responses/{recipe_id}/", f"{item_name}.json"), mode="w") as f:
                json.dump(result, f)
        except FileNotFoundError:
            print("Creating the folder for local cache...")
            os.mkdir(f"./recipe_integration/static/samples/api_responses/{recipe_id}/")
            with open(os.path.join(f"./recipe_integration/static/samples/api_responses/{recipe_id}/", f"{item_name}.json"), mode="w") as f:
                json.dump(result, f)
    return result


def get_saved_api_response(recipe_id, item_name):
    with open(os.path.join(f"./recipe_integration/static/samples/api_responses/{recipe_id}/", f"{item_name}.json"), mode="r") as f:
        data = json.loads(f.read())
    return data


def get_ingredients(recipe_id):
    with open(os.path.join("./recipe_integration/static/samples/recipes/", f"{recipe_id}.json"), mode="r") as f:
        json_data = f.read()
    data = json.loads(json_data)
    return data["Name"], data["Servings"], data["Ingredients"], data["Amount"]

def get_result(item_name, item_amount, recipe_id, local_cache=False):
    import time
    data = None
    if local_cache:
        try:
            data = get_saved_api_response(item_name=item_name, recipe_id=recipe_id)
            print(data)
        except BaseException as e:
            print(e)
            print("No local cache found... Getting the data from API...")
            time.sleep(3)
            data = get_api_response(item_name=item_name, recipe_id=recipe_id, save=True)
    else:
        data = get_api_response(item_name=item_name, recipe_id=recipe_id, save=False)
    items = data["Items"]
    main_info = []
    for item in items[:10]:
        main_info.append(
            {
                "product_name": item_name,
                "product_amount": item_amount,
                "img": item["Item"]["smallImageUrls"][0]["imageUrl"],
                "mediumImg": item["Item"]["mediumImageUrls"][0]["imageUrl"],
                "name": item["Item"]["itemName"],
                "price": item["Item"]["itemPrice"],
                "url": item["Item"]["itemUrl"],
                "score": item["Item"]["reviewAverage"],
            }
        )
    return main_info
