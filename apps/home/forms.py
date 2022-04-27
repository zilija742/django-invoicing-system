from dataclasses import field
from django import forms
from .models import EntitiesModel

class EntitiesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntitiesForm, self).__init__(*args, **kwargs)
        
        #Set field label
        self.fields['number'].label = "Número (RUC, DNI, Etc) "
        self.fields['type'].label = "Tipo"
        self.fields['full_name'].label = "Razón social o nombre completo "
        self.fields['brand'].label = "Razón comercial (Marca)"
        self.fields['address'].label = "Dirección fiscal"
        self.fields['primary_email'].label = "Email principal"
        self.fields['first_email'].label = "1er Email opcional"
        self.fields['second_email'].label = "2do Email opcional"
        self.fields['mobile_number'].label = "Móvil (opcional)"
        self.fields['fijo'].label = "Fijo (opcional)"
        self.fields['client_detraccion'].label = "N. Cta. detracción del cliente"
        self.fields['detail'].label = "Detalle adicional (opcional)"

        #Set required
        self.fields['brand'].required = False
        self.fields['address'].required = False
        self.fields['primary_email'].required = False
        self.fields['first_email'].required = False
        self.fields['second_email'].required = False
        self.fields['mobile_number'].required = False
        self.fields['fijo'].required = False
        self.fields['client_detraccion'].required = False
        self.fields['detail'].required = False

    number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    type = forms.CharField(
        widget=forms.Select(
            choices=[
                ('', 'Elegir'),
                (1, '6 RUC - REGISTRO ÚNICO DE CONTRIBUYENTE'),
                (2, '1 DNI - DOC. NACIONAL DE IDENTIDAD'),
                (3, '- VARIOS - VENTAS MENORES A S/.700.00 Y OTROS'),
                (4, '4 CARNET DE EXTRANJERÍA'),
                (5, '7 PASAPORTE'),
                (6, 'A CÉDULA DIPLOMATICA DE IDENTIDAD'),
                (7, '0 NO DOMICILIADO, SIN RUC (EXPORTACIÓN)'),
                (8, 'B DOC. IDENT. PAIS. RESIDENCIA-NO.D'),
                (9, 'C Tax Identification Number - TIN – Doc Trib PP.NN'),
                (10, 'D Identification Number - IN – Doc Trib PP.JJ'),
            ],
            attrs={
                "class": "form-control"
            }
        ))

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    brand = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    primary_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        ))

    first_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        ))

    second_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        ))

    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    fijo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    client_detraccion = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    detail = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))
    
    class Meta:
        model = EntitiesModel
        fields = "__all__"
        exclude = ['user_id']