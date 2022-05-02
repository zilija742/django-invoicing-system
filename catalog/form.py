from dataclasses import fields
from django import forms
from .models import CategoriesModel, CatalogsModel

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

class CatalogsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CatalogsForm, self).__init__(*args, **kwargs)
        
        self.fields['category'] = forms.ModelChoiceField(
            queryset=CategoriesModel.objects.filter(user_id=user.id),
            widget=forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            initial=0,
            label='Categoría'
        )
        self.fields['type'] = forms.IntegerField(
            widget=forms.Select(
                choices=[
                    (None, 'Elegir'),
                    (1, 'NIU - PRODUCTO'),
                    (2, 'ZZ - SERVICIO'),
                ],
                attrs={
                    "class": "form-control"
                }
            ),
            label='Tipo'
        )
        self.fields['code'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            label='Código interno'
        )
        self.fields['name'] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            label='Nombre del producto o servicio'
        )
        self.fields['sunat_code'] = forms.IntegerField(
            widget=forms.Select(
                choices=[
                    (None, 'Elegir'),
                    (10101501, '10101501 - Gatos'),
                    (10101502, '10101502 - Perros'),
                ],
                attrs={
                    "class": "form-control"
                }
            ),
            label='Código Producto Sunat'
        )
        self.fields['currency'] = forms.IntegerField(
            widget=forms.Select(
                choices=[
                    (1, 'SOLES'),
                    (2, 'DÓLARES AMERICANOS'),
                    (3, 'EUROS')
                ],
                attrs={"class": "form-control"}
            ),
            label='Moneda (Referencial)',
            required=False
        )
        self.fields['affectation_type'] = forms.IntegerField(
            widget=forms.Select(
                choices=[
                    (None, "legir un tipo"),
                    (1, "10-Gravado - Operación Onerosa [10]"),
                    (2, "11-[Gratuita] Gravado – Retiro por premio [11]"),
                    (3, "12-[Gratuita] Gravado – Retiro por donación [12]"),
                    (4, "13-[Gratuita] Gravado – Retiro [13]"),
                    (5, "14-[Gratuita] Gravado – Retiro por publicidad [14]"),
                    (6, "15-[Gratuita] Gravado – Bonificaciones [15]"),
                    (7, "16-[Gratuita] Gravado – Retiro por entrega a trabajadores [16]"),
                    (8, "20-Exonerado - Operación Onerosa [20]"),
                    (9, "30-Inafecto - Operación Onerosa [30]"),
                    (10, "31-[Gratuita] Inafecto – Retiro por Bonificación [31]"),
                    (11, "32-[Gratuita] Inafecto – Retiro [32]"),
                    (12, "33-[Gratuita] Inafecto – Retiro por Muestras Médicas [33]"),
                    (13, "34-[Gratuita] Inafecto - Retiro por Convenio Colectivo [34]"),
                    (14, "35-[Gratuita] Inafecto – Retiro por premio [35]"),
                    (15, "36-[Gratuita] Inafecto - Retiro por publicidad [36]"),
                    (16, "40-Exportación [40]"),
                    (17, "21-[Gratuita] Exonerado - Transferencia gratuita [21]"),
                    (18, "17-Gravado - IVAP [17]"),
                    (19, "101-[Gratuita] Gravado - IVAP [101]"),
                ],
                attrs={"class": "form-control"}
            ),
            label='Tipo de afectación (Opcional)',
            required=False
        )
        self.fields['sale_without_igv'] = forms.IntegerField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            label='VALOR VENTA unitario SIN IGV (al que se venderá)',
            required=False
        )
        self.fields['sale_with_igv'] = forms.IntegerField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            label='PRECIO VENTA unitario CON IGV (al que se venderá)',
            required=False
        )
        self.fields['purchase_without_igv'] = forms.IntegerField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            label='VALOR COMPRA unitario SIN IGV (al que se compró)',
            required=False
        )
        self.fields['purchase_with_igv'] = forms.IntegerField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            label='PRECIO COMPRA unitario CON IGV (al que se compró)',
            required=False
        )

    class Meta:
        model = CatalogsModel
        fields = "__all__"
        exclude = ['user_id']