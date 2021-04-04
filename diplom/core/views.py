from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Zayavka
from .forms import ZayavkaForm

def main(request):
    return render(request, 'core/main.html')


def about(request):
    return render(request, 'core/about.html')


def new_appl(request):
    return render(request, 'core/new_appl.html')


def login(request):
    return render(request, 'core/login.html')


# def employee(request):
#     return render(request, 'core/employee.html')


# получение данных из бд
def index(request):
    zayavki = Zayavka.objects.all()
    return render(request, 'core/employee.html', {"zayavki": zayavki})


# сохранение данных в бд
def create(request):
    form = ZayavkaForm()

    data = {
        'form': form
    }
    return render(request, 'core/new_application.html', data)


