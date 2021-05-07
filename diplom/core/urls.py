from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_main, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('new_application', views.createZayavka, name='new_appl'),
    path('new_client', views.createClient, name='new_cli'),
    path('<int:pk>', views.KvartDelailView.as_view(), name='kvartdeteil'),
    path('employee', views.employee, name='employee')
]
