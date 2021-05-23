from django.urls import path

from . import views

urlpatterns = [

    path('', views.list_main, name='home'),
    path('about', views.about, name='about'),
    path('kvartdetail/<int:pk>', views.KvartDelailView.as_view(), name='kvartdetail'),  # по квартире
    path('new_client/<int:id_kv>', views.createClient, name='new_cli'),  # Для нового клиента
    path('new_zayavka/<int:id_kv>/<int:kod_client>', views.createZayavka, name='new_zayavka'),  # Для новой заявки
    path('appl_inf/<int:id_kv>/<int:kod_client>/<int:id_zaya>', views.ZayaInf, name='appl_inf'),  # Информация о заявке
    path('zayavka/', views.SearchZaya, name='zayavka_inf'),  # ввод данных для вывода заявки
    path('information/<int:pk>', views.ZayavkaV.as_view(), name='information'),  # вывод информации по заявке



]
