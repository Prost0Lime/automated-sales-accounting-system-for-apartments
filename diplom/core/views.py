from django.shortcuts import render, redirect
from .models import *
from .forms import ZayavkaForm
from django.views.generic import DetailView
from django.views.generic import ListView


def about(request):
    return render(request, 'core/about.html')


def login(request):
    return render(request, 'core/login.html')


# получение данных из бд заявки
def index(request):
    zayavki = Zayavka.objects.all()
    return render(request, 'core/employee.html', {'zayavki': zayavki})


# сохранение данных в бд
def create(request):
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
        'form': form,
        'error': error
    }
    return render(request, 'core/new_appl.html', data)


# вывод квартир на главный экран
def list_main(request):
    menu = Kvart.objects.all()
    return render(request, 'core/main.html', {'menu': menu})


# Детали квартиры
class KvartDelailView(DetailView):
    model = KvartV
    template_name = 'core/kvartdetail.html'
    context_object_name = 'kv_v'
