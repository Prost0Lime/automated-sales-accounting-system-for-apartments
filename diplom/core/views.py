from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import DetailView


def about(request):
    return render(request, 'core/about.html')


# получение данных из бд заявки панель сотрудника
def employee(request):
    zayavka = Zayavka.objects.all()
    return render(request, 'core/employee.html', {'zayavka': zayavka})


# сохранение данных в бд Новая заявка
def createZayavka(request):
    error = ''
    if request.method == 'POST':
        form = ZayavkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена не правильно'

    form = ZayavkaForm()

    data = {
        'formZ': form,
        'error': error
    }

    return render(request, 'core/new_appl.html', data)


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


# вывод квартир на главный экран
def list_main(request):
    menu = Kvart.objects.all()
    return render(request, 'core/main.html', {'menu': menu})


# Детали квартиры
class KvartDelailView(DetailView):
    model = KvartV
    template_name = 'core/kvartdetail.html'
    context_object_name = 'kv_v'
