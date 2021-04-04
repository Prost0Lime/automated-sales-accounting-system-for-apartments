from .models import Zayavka
from django.forms import ModelForm, TextInput, DateInput, Select


class ZayavkaForm(ModelForm):
    class Meta:
        model = Zayavka
        fields = ['data_zaya', 'opisanie', 'kod_client', 'kod_sotrudn']

        widgets = {
            "data_zaya": DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Дата заявки'
            }),
            "opisanie": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
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