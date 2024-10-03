from django import forms


class RecipeFetchForm(forms.Form):
    recipe_id = forms.IntegerField(widget=forms.TextInput(), required=True)


