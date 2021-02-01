from django.shortcuts import render


def main(request):
    return render(request, 'core/main.html')


def about(request):
    return render(request, 'core/about.html')
