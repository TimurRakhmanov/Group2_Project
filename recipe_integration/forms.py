from django import forms


class RecipeFetchForm(forms.Form):
    recipe_id = forms.IntegerField(widget=forms.TextInput(attrs={"required": True, "type": "number", "min": 0,}), required=True, label="Recipe ID")
