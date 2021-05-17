from .models import *
from django.forms import ModelForm, TextInput, DateInput, Select


class ZayavkaForm(ModelForm):
    class Meta:
        model = Zayavka
        fields = ['data_zaya', 'id_kv', 'kod_client', 'kod_sotrudn']

        widgets = {

            "data_zaya": DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Дата заявки',

            }),
            "id_kv": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ид квартиры',
                'readonly': True
            }),
            "kod_client": TextInput(attrs={
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
        CHOICES = [('Физическое', 'Физическое'), ('Юридическое', 'Юридическое')]
        model = Client
        fields = ['kod_client', 'pasp', 'fio_client', 'phone', 'status']

        widgets = {
            "kod_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код клиента'
            }),
            "pasp": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серия, номер паспорта',
                'id': 'pasp'
            }),
            "fio_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
                'id': 'phone'
            }),
            "status": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Статус',
                'id': 'status'
            }, choices=CHOICES)

        }
