from django.test import TestCase
from . import models, forms

class Test(TestCase):
    def test_account_create(self):
        valid_user = {
                    "username": "Test",
                    "email": "test@gmail.com",
                    "password1": "prewads@1232#1",
                    "password2": "prewads@1232#1",
                    "msg": "Valid Credentials",
                }
        
        invalid_users = [
            {
                "username": "",
                "email": "test@gmail.com",
                "password1": "test@1232#1",
                "password2": "test@1232#1",
                "msg": "Empty Username",
            },
            {
                "username": "ADswqdw",
                "email": "tewqdst@gmail.com",
                "password1": "",
                "password2": "",
                "msg": "Empty Password",
            },
            {
                "username": "Test",
                "email": "test@gmail.com",
                "password1": "te#1",
                "password2": "te#1",
                "msg": "Short Password",
            },
            {
                "username": "Test",
                "email": "test@gmail.com",
                "password1": "te#1",
                "password2": "te#2",
                "msg": "Password Mismatch",
            },
            
            {
                "username": "Test",
                "email": "testgmail.com",
                "password1": "test@1232#1",
                "password2": "test@1232#1",
                "msg": "Invalid Email"
            },
            {
                "username": "Used",
                "email": "asddwq@gmail.com",
                "password1": "asd@das#1",
                "password2": "asd@das#1",
                "msg": "Username is already used",
            },
            {
                "username": "Test1234",
                "email": "test1234@gmail.com",
                "password1": "test1234",
                "password2": "test1234",
                "msg": "Password is not secure enough",
            },
        ]
        
        models.User.objects.create_user(username="Used", email="used@gmail.com", password="123124dsads2@")
        
        users = [valid_user]
        users.extend(invalid_users)
        invalid_results = [False for i in range(len(invalid_users))]
        expeted_result = [True,]
        expeted_result.extend(invalid_results)

        for idx, user in enumerate(users):
            msg = user.pop("msg")
            form = forms.UserCreationCustomForm(data=user)
            self.assertEquals(form.is_valid(), expeted_result[idx], msg)
