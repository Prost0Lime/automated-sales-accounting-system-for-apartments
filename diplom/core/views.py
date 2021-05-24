from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import DetailView


def about(request):
    return render(request, 'core/about.html')


# вывод квартир
def list_main(request):
    menu = Kvart.objects.all()
    return render(request, 'core/main.html', {'menu': menu})


# Детали квартиры
class KvartDelailView(DetailView):
    model = KvartV
    template_name = 'core/kvartdetail.html'
    context_object_name = 'kv_v'


# сохранение данных в бд Новый клиент
def createClient(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_appl')
        else:
            error = 'Форма заполнена не правильно'

    form = ClientForm()

    data = {
        'formC': form,
        'error': error
    }
    return render(request, 'core/new_client.html', data)


# сохранение данных в бд Новая заявка
def createZayavka(request, id_kv: int, kod_client: int):
    error = ''
    if request.method == 'POST':
        form = ZayavkaForm(request.POST)
        if form.is_valid():
            form.save()
            id_zaya = form.instance.id_zaya
            return redirect('appl_inf', id_kv=id_kv, kod_client=kod_client, id_zaya=id_zaya)
        else:
            error = 'Форма заполнена не правильно'

    form = ZayavkaForm(initial={'id_kv': Kvart.objects.get(id_kv=id_kv),
                                'kod_client': Client.objects.get(kod_client=kod_client)})

    data = {
        'formZ': form,
        'error': error,

    }
    return render(request, 'core/new_appl.html', data)


# вывод информации о заполненной заявке
def ZayaInf(request, id_kv: int, kod_client: int, id_zaya: int):
    form = ZayavkaForm(initial={'id_kv': Kvart.objects.get(id_kv=id_kv),
                                'kod_client': Client.objects.get(kod_client=kod_client)})
    data = {
        'formZ': form,
        'id_zaya': id_zaya,

    }
    return render(request, 'core/appl_inf.html', data)


# Поиск заявки
def SearchZaya(request):
    error = ''
    if request.method == 'POST':
        form = ZayaInfForm(request.POST)
        if form.is_valid():
            id_zaya = form.cleaned_data["id_zaya"]
            pasp = form.cleaned_data["pasp"]
            return redirect('information', pk=id_zaya, pasp=pasp)
        else:
            error = 'Форма заполнена не правильно'

    form = ZayaInfForm()

    data = {
        'formS': form,
        'error': error,

    }

    return render(request, 'core/search_zaya.html', data)


# вывод информации о заявке по поиску
class ZayavkaV(DetailView):
    model = ZayavkaV
    template_name = 'core/information.html'
    context_object_name = 'zaya'

    def get(self, request, pk, pasp, *args, **kwargs):
        print(pk, pasp)
        return super(ZayavkaV, self).get(request, *args, **kwargs)
