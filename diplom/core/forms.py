from .models import Zayavka
from django.forms import ModelForm

class ZayavkaForm(ModelForm):
    class Meta:
        model = Zayavka
        fields = ['data_zaya', 'opisanie', 'kod_client', 'kod_sotrudn']