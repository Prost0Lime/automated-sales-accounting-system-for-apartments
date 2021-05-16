from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_main, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('new_zayavka/<int:id_kv>/<int:kod_client>', views.createZayavka, name='new_zayavka'), #Для новой заявки
    path('new_client/<int:id_kv>', views.createClient, name='new_cli'),  #Для нового клиента
    path('kvartdetail/<int:pk>', views.KvartDelailView.as_view(), name='kvartdetail'),  #по квартире
    path('employee', views.employee, name='employee')
]
