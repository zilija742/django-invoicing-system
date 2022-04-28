from django import forms
from .models import CategoriesModel

class CategoriesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoriesForm, self).__init__(*args, **kwargs)

        self.fields['category_code'].label = "Código"
        self.fields['category_description'].label = "Descripción"

    category_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    category_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = CategoriesModel
        fields = "__all__"
        exclude = ['user_id']