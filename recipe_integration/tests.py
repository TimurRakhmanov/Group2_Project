from django.test import TestCase
from . import forms, utils
from accounts import models
import os


class Test(TestCase):
    def test_main(self):
        valid_user = {
            "username": "Test",
            "email": "test@gmail.com",
            "password": "test@1232#1",
        }

        invalid_user = {
            "username": "s",
            "email": "test@gmail.com",
            "password": "test@#1",
        }
        
        users = [valid_user, invalid_user]
        expected_status_codes = [200, 302]
        models.User.objects.create_user(**valid_user)

        for idx, user in enumerate(users):
            self.client.login(**user)
            response = self.client.get("http://127.0.0.1:8000/integration/recipe/")
            self.assertEquals(response.status_code, expected_status_codes[idx])
            self.client.logout()

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

