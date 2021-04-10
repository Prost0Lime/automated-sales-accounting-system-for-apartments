from .models import Zayavka
from django.forms import ModelForm, TextInput, DateInput, Select


class ZayavkaForm(ModelForm):
    class Meta:
        model = Zayavka
        fields = ['data_zaya', 'id_kv', 'kod_client', 'kod_sotrudn']

        widgets = {
            "data_zaya": DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Дата заявки'
            }),
            "id_kv": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Ид квартиры'
            }),

            "kod_client": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Код клиента'
            }),
            "kod_sotrudn": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Код сотрудника'
            })
        }