from dataclasses import fields
from django import forms
from pkg_resources import require
from catalog.models import CatalogsModel

from purchase.models import PurchasesModel

class PurchasesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PurchasesForm, self).__init__(*args, **kwargs)

        self.fields['entity'] = forms.ModelChoiceField(
            queryset=PurchasesModel.objects.filter(user_id=user.id),
            widget=forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            label='Buscar Proveedor'
        )

        self.fields['document_type'] = forms.IntegerField(
            widget=forms.Select(
                choices=[
                    (None, 'Elegir documento'),
                    (1, 'FACTURA'),
                    (2, 'BOLETA DE VENTA'),
                    (3, 'LIQUIDACIÓN DE COMPRA')
                ],
                attrs={
                    "class": "form-control"
                }
            ),
            label='Tipo documento'
        )

        self.fields['broadcast_date'] = forms.DateField(
            widget=forms.TextInput(
                attrs={
                    "class": "form_control"
                }
            ),
            label="Fecha emisión"
        )

        self.fields['currency'] = forms.IntegerField(
            widget=forms.Select(
                choices=[
                    (1, 'S/'),
                    (2, 'US$'),
                    (3, '€')
                ],
                attrs={
                    "class": "form-control"
                }
            ),
            label='Moneda'
        )

        self.fields['exchange_rate'] = forms.DecimalField(
            widget=forms.TextInput(
                attrs={
                    "class": "form_control"
                }
            ),
            label='Tipo de cambio',
            required=False
        )

        self.fields['series'] = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
            ),
            label='Serie'
        )

        self.fields['number'] = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control"}
            ),
            label='Número'
        )

        self.fields['catalog'] = forms.ModelChoiceField(
            queryset=CatalogsModel.objects.filter(user_id=user.id),
            widget=forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            label='Buscar en catálog, PRODUCTO o SERVICIO'
        )

    class Meta:
        model = PurchasesModel
        fields = "__all__"
        exclude = ['user_id']