from .models import *
from django.forms import ModelForm, TextInput, DateInput, Select


class ZayavkaForm(ModelForm):
    class Meta:
        model = Zayavka
        fields = ['num_zaya', 'data_zaya', 'id_kv', 'kod_client', 'kod_sotrudn']

        widgets = {
            "num_zaya": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Номер заявки'
        }),

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


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['kod_client', 'pasp', 'fio_client', 'phone', 'status']

        widgets = {
            "kod_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код клиента'
            }),
            "pasp": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия, номер паспорта'
            }),
            "fio_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус'
            })

        }
