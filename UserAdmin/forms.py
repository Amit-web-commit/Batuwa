from django import forms
from .models import Categories


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'})
        }
    