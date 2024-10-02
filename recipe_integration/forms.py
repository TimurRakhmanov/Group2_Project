from django import forms


class RecipeFeatchForm(forms.Form):
    recipe_id = forms.IntegerField(widget=forms.TextInput(), required=True)


