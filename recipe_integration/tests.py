from django.test import TestCase
import unittest

class Test(TestCase):
    def test_main(self):
        response = self.client.get("http://127.0.0.1:8000/integration/recipe/")
        self.assertEquals(response.status_code, 200)

    def test_input_id(self):
        response = self.client.post("http://127.0.0.1:8000/integration/recipe/wqeqw")