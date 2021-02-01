from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render( request, 'core/main.html')


def about(request):
    return render( request, 'core/about.html')
