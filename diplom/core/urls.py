from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_main, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('emlpoyee', views.index, name='employee'),
    path('new_appl', views.create, name='new_appl'),

]
