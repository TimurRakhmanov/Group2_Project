from django.test import TestCase
from . import forms, utils
import os


class Test(TestCase):
    def test_main(self):
        response = self.client.get("http://127.0.0.1:8000/integration/recipe/")
        self.assertEquals(response.status_code, 200)

    def test_RecipeFetchForm(self):
        invalid_data_samples = [
            {"recipe_id": "abssd", "msg": "Characters only"},
            {"recipe_id": "1asd", "msg": "Numbers and characters"},
            {"recipe_id": "12312321312312312312a", "msg": "Long number and character"},
            {"recipe_id": "-123", "msg": "Negative numbers"},
            {"recipe_id": "-asd", "msg": "Negative characters"},
            {"recipe_id": "-@さ", "msg": "Symbols and Japanese characters"},
            
        ]
        for invalid_sample in invalid_data_samples:
            invalid_form = forms.RecipeFetchForm(data=invalid_sample)
            self.assertEquals(invalid_form.is_valid(), False)

    def test_utils_ingredients(self):
        import time
        import json
        recipe_dir_path = "./recipe_integration/static/samples/recipes/"
        recipe_dir = os.scandir(recipe_dir_path)
        for file in recipe_dir:
            recipe_id = file.name.strip(".json")
            _, _, ingredients, amount = utils.get_ingredients(recipe_id=recipe_id)
            for ingredient in ingredients:
                saved_resp = utils.get_result(item_name=ingredient, item_amount=amount, recipe_id=recipe_id, local_cache=True)
                # rt_resp = utils.get_api_response(item_name=ingredient, recipe_id=recipe_id, save=False)
                # time.sleep(2)
                # self.assertJSONEqual(json.loads(saved_resp), json.loads(rt_resp))
