import json
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

def get_api_response(item_name, recipe_id, save=False):
    request_url = """https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601/"""
    params={
        "format": "json", 
        "keyword": item_name, 
        "applicationId": os.getenv("APP_ID"),
        "availability": 1,
        "imageFlag": 1,
        "appointDeliveryDateFlag": 1,
        "elements": "smallImageUrls,mediumImageUrls,itemName,itemPrice,itemUrl,reviewAverage"
    }   
    # Comment the lines used for profiling the requests
    # for i in range(10):
        # t1 = time.time()
    result = requests.get(request_url, params=params)
        # t2 = time.time()
        # delta = t2 - t1
        # if params.get("elements") is not None:
        #     with open(f"./recipe_integration/profiling/short/{recipe_id}.txt", mode="a") as f:
        #         f.writelines(f"{i}, {item_name}, {delta}\n")
        # else:
        #     with open(f"./recipe_integration/profiling/full/{recipe_id}.txt", mode="a") as f:
        #         f.writelines(f"{i}, {item_name}, {delta}\n")
        # time.sleep(3)
    result = result.json()
    # Save if there is no cache
    if save:
        try:
            with open(os.path.join(f"./recipe_integration/static/samples/api_responses/{recipe_id}/", f"{item_name}.json"), mode="w") as f:
                json.dump(result, f)
        except FileNotFoundError:
            # Create the appropriate directory to store the cache data
            print("Creating the folder for local cache...")
            os.mkdir(f"./recipe_integration/static/samples/api_responses/{recipe_id}/")
            with open(os.path.join(f"./recipe_integration/static/samples/api_responses/{recipe_id}/", f"{item_name}.json"), mode="w") as f:
                json.dump(result, f)
    return result


def get_saved_api_response(recipe_id, item_name):
    # This function is used to retrieve the data from cache
    with open(os.path.join(f"./recipe_integration/static/samples/api_responses/{recipe_id}/", f"{item_name}.json"), mode="r") as f:
        data = json.loads(f.read())
    return data


def get_ingredients(recipe_id):
    # Get the ingredients from the sample data
    with open(os.path.join(f".{os.path.sep}recipe_integration{os.path.sep}static{os.path.sep}samples{os.path.sep}recipes{os.path.sep}", f"{recipe_id}.json"), mode="r", encoding="utf-8_sig") as f:
        json_data = f.read()
    data = json.loads(json_data)
    return data["Name"], data["Servings"], data["Ingredients"], data["Amount"]

def get_result(item_name, item_amount, recipe_id, local_cache=False):
    import time
    data = None
    if local_cache:
        try:
            data = get_saved_api_response(item_name=item_name, recipe_id=recipe_id)
        except BaseException as e:
            print(e)
            print("No local cache found... Getting the data from API...")
            # Sleep to prevent the connection disconnect from the API source
            time.sleep(3)
            data = get_api_response(item_name=item_name, recipe_id=recipe_id, save=True)
    else:
        data = get_api_response(item_name=item_name, recipe_id=recipe_id, save=False)
    items = data["Items"]
    main_info = []
    # Show only the 10 itimes
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
