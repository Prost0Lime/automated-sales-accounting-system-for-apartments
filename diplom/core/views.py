from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Zayavka
from .models import Client
from .models import Sotrudn


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
    return render(request, "core/employee.html", {"zayavki": zayavki})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Zayavka()
        # tom = Client()
        # tom = Sotrudn()
        tom.id_zaya = request.POST.get("id_zaya")
        tom.data_zaya = request.POST.get("data_zaya")
        tom.opisanie = request.POST.get("opisanie")
        tom.kod_client = request.POST.get("kod_client")
        tom.kod_sotrudn = request.POST.get("kod_sotrudn")
        tom.save()
    return HttpResponseRedirect("new_application")
